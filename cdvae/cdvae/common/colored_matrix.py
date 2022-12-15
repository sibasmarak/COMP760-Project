import torch, pickle

from constants import Ptriclinic_generator, Cubic_generator

def create_colored_matrix(input_generators, output_generators):
    assert len(input_generators) == len(output_generators)
    assert len(input_generators) > 0
    p = len(input_generators)
    n = len(input_generators[0])
    m = len(output_generators[0])
    colors = {}
    for i in range(n):
        for j in range(m):
            colors[(i, j)] = i * m + j
    while True:
        old_colors = colors.copy()
        for k in range(p):
            input_gen = input_generators[k]
            output_gen = output_generators[k]
            for i in range(n):
                for j in range(m):
                    colors[(i, j)] = min(
                        colors[(i, j)], colors[(input_gen[i], output_gen[j])]
                    )
                    colors[(input_gen[i], output_gen[j])] = colors[(i, j)]
        if colors == old_colors:
            break
    colors_list = sorted(list(set(colors.values())))
    num_colors = len(colors_list) # number of unique colors after changing the colors of the matrix
    # make colors be consecutive integers from 0 to `num_colors` - 1
    color_to_idx = {colors_list[i]: i for i in range(num_colors)}
    for k, v in colors.items():
        colors[k] = color_to_idx[v]
    assert min(colors.values()) == 0
    assert max(colors.values()) == num_colors - 1
    return colors

colored_matrices = {}
generators = {'ptriclinic': Ptriclinic_generator, 'pcubic': Cubic_generator}

for key, gen in generators.items():
    colored_matrix_dict = create_colored_matrix(gen, gen)
    
    # convert colored matrix dict to matrix
    n = len(gen[0])
    m = len(gen[0])
    colored_matrix = torch.zeros((n, m))
    for k, v in colored_matrix_dict.items():
        colored_matrix[k] = int(v)

    if key == 'ptriclinic':
        # replicate to get 40x40 matrix
        colored_matrix = torch.cat([colored_matrix] * 5, dim=0)
        colored_matrix = torch.cat([colored_matrix] * 5, dim=1)

        assert colored_matrix.shape == (40, 40)

    colored_matrices[key] = colored_matrix

pickle.dump(colored_matrices, open('colored_matrices.pkl', 'wb'))


