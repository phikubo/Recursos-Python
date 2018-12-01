#cortesia de edx, 
#modificado por phikubo para importa modulo sin errores
def plot_prediction_grid (xx, yy, prediction_grid, filename, predictors, outcomes):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    import matplotlib.pyplot as plt
    import numpy as np
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)
   
if __name__ == "__main__":
	pass
else:
	print("modulo importado Caso 3: Ploteo de colores")
