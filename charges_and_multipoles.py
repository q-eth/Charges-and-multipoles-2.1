import numpy as np

def point_charge_field(Q, charge_pos, x_m, y_m, z_m):
    x_c, y_c, z_c = charge_pos
    r_vec = np.array([x_m - x_c, y_m - y_c, z_m - z_c])
    r_mgn = np.linalg.norm(r_vec)
    
    if r_mgn == 0:
        return np.array([np.nan, np.nan, np.nan])
    
    E = Q * r_vec / r_mgn**3
    return E

def point_charge_potential(Q, charge_pos, x_m, y_m, z_m):
    x_c, y_c, z_c = charge_pos
    r_vec = np.array([x_m - x_c, y_m - y_c, z_m - z_c])
    r_mgn = np.linalg.norm(r_vec)
    
    if r_mgn == 0:
        return np.nan
    
    Phi = Q / r_mgn
    return Phi

print("Electric field: ", point_charge_field(1, [0, 0, 0], 2, 2, 2))
print("Potential is: ", point_charge_potential(1, [0, 0, 0], 2, 2, 2))