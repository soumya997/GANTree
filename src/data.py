import numpy as np


class DataLoader(object):

    def broken_circle(self):
        new_data = []
        num_samples = 10000
        train_ratio = 0.8
        theta = np.random.uniform(0, 2 * np.pi, num_samples)
        num_samples = theta.shape[0]
        n_train = int(train_ratio * num_samples)

        filter_theta = [
            [0, 15],
            [345, 360],
            [75, 95],
            [120, 139],
            [200, 270]
        ]

        theta = filter(lambda x: any([r[0] <= x * 180 / np.pi <= r[1] for r in filter_theta]), theta)

        r = 1

        if n == 1:
            points = np.transpose(np.array([r * np.cos(theta), r * np.sin(theta)]))
            new_data = np.array(points)
            n_train = int(train_ratio * new_data.shape[0])
            training, test = new_data[:n_train, :], new_data[n_train:, :]

            return training, test
