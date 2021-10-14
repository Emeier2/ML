
import sys
import math
import Node
class DecisionTreeClassifier:

    def __init__(self, X, feature_names, labels):
        self.X = X  # features or predictors
        self.feature_names = feature_names  # name of the features
        self.labels = labels  # categories
        self.labelCategories = list(set(labels))  # unique categories
        # number of instances of each category
        self.labelCategoriesCount = [list(labels).count(x) for x in self.labelCategories]
        self.node = None  # nodes
        # calculate the initial entropy of the system
        self.entropy = self._get_entropy([x for x in range(len(self.labels))])
    
    def _get_entropy(self, x_ids):
        # sorted labels by instance id
        labels = [self.labels[i] for i in x_ids]
        # count number of instances of each category
        label_count = [labels.count(x) for x in self.labelCategories]
        # calculate the entropy for each category and sum them
        entropy = sum([-count / len(x_ids) * math.log(count / len(x_ids), 2)
                    if count else 0
                    for count in label_count
                    ])
            
        return entropy
    def _get_information_gain(self, x_ids, feature_id):
        # calculate total entropy
        info_gain = self._get_entropy(x_ids)
        # store in a list all the values of the chosen feature
        x_features = [self.X[x][feature_id] for x in x_ids]
        # get unique values
        feature_vals = list(set(x_features))
        # get frequency of each value
        feature_v_count = [x_features.count(x) for x in feature_vals]
        # get the feature values ids
        feature_v_id = [
            [x_ids[i]
            for i, x in enumerate(x_features)
            if x == y]
            for y in feature_vals
        ]

        # compute the information gain with the chosen feature
        info_gain_feature = sum([v_counts / len(x_ids) * self._get_entropy(v_ids)
                            for v_counts, v_ids in zip(feature_v_count, feature_v_id)])

        info_gain = info_gain - info_gain_feature

        return info_gain
    def _get_feature_max_information_gain(self, x_ids, feature_ids):
        
        # get the entropy for each feature
        features_entropy = [self._get_information_gain(x_ids, feature_id) for feature_id in feature_ids]
        # find the feature that maximises the information gain
        max_id = feature_ids[features_entropy.index(max(features_entropy))]

        return self.feature_names[max_id], max_id

    def id3(self):
        # assign an unique number to each instance
        x_ids = [x for x in range(len(self.X))]
        # assign an unique number to each featuer
        feature_ids = [x for x in range(len(self.feature_names))]
        # define node variable - instance of the class Node
        self.node = self._id3_recv(x_ids, feature_ids, self.node)
        
    def _id3_recv(self, x_ids, feature_ids, node):
        if not node:
            node = Node()  # initialize nodes
        # sorted labels by instance id
        labels_in_features = [self.labels[x] for x in x_ids]
        # if all the example have the same class (pure node), return node
        if len(set(labels_in_features)) == 1:
            node.value = self.labels[x_ids[0]]
            return node
        # if there are not more feature to compute, return node with the most probable class
        if len(feature_ids) == 0:
            node.value = max(set(labels_in_features), key=labels_in_features.count)  # compute mode
            return node
        # else...
        # choose the feature that maximizes the information gain
        best_feature_name, best_feature_id = self._get_feature_max_information_gain(x_ids, feature_ids)
        node.value = best_feature_name
        node.childs = []
        # value of the chosen feature for each instance
        feature_values = list(set([self.X[x][best_feature_id] for x in x_ids]))
        # loop through all the values
        for value in feature_values:
            child = Node()
            child.value = value  # add a branch from the node to each feature value in our feature
            node.childs.append(child)  # append new child node to current node
            child_x_ids = [x for x in x_ids if self.X[x][best_feature_id] == value]
            if not child_x_ids:
                child.next = max(set(labels_in_features), key=labels_in_features.count)
                print('')
            else:
                if feature_ids and best_feature_id in feature_ids:
                    to_remove = feature_ids.index(best_feature_id)
                    feature_ids.pop(to_remove)
                # recursively call the algorithm
                child.next = self._id3_recv(child_x_ids, feature_ids, child.next)
        return node
    def find_outcome(self, input):
        ##take input, read through array, follow key points down to conclusion
        return 