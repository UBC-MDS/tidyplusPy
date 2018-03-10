""" tidyplusPy.imputations.mmm"""

import random
import numpy as np



def mmm(data, method):
    """Multivariate Imputation by Mode
    ----------
    data: numpy.ndarray
        Data to impute.
    method : could be Mean,Median,Mode
    RETURNS
    -------
    numpy.ndarray
        Imputed data.
    """
    null_xy = find_null(data)

    # Add a column of zeros to the index values
    null_xyv = np.append(null_xy, np.zeros((np.shape(null_xy)[0], 1)), axis=1)

    null_xyv = [[int(x), int(y), v] for x, y, v in null_xyv]
    temp = []
    cols_missing = set([y for _, y, _ in null_xyv])


        # Step 2: Missing values for the missing variable/column are replaced
        # with predictions from our new linear regression model
        temp = []
        # For null indices with the dependent column that was randomly chosen
        for i, x_i, y_i, value in enumerate(null_xyv):
            if y_i == dependent_col:
                # Row 'x' without the nan value
                new_value = model.predict(np.delete(data[x_i], dependent_col))
                data[x_i][y_i] = new_value.reshape(1, -1)
                temp.append([x_i, y_i, new_value])
                delta = (new_value-value)/value
                if delta < 0.1:
                    converged[i] = True
        null_xyv = temp
    return data