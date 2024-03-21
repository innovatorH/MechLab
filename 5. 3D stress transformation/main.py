# importing the neccessary modules
from pyscript import document
from pyscript import display
import matplotlib.pyplot as plt
import numpy as np
import js


def calculate(*args, **kwargs):

    
    sigma_x = document.querySelector("#sigma_x").value
    sigma_y = document.querySelector("#sigma_y").value
    sigma_z = document.querySelector("#sigma_z").value
    tau_xy = document.querySelector("#tau_xy").value
    tau_yz = document.querySelector("#tau_yz").value
    tau_xz = document.querySelector("#tau_xz").value
    unit = document.querySelector("#unit").value
    w = document.querySelector("#w").value

    if sigma_x == "" or sigma_y == "" or sigma_z == "" or tau_xy == "" or tau_yz == "" or tau_xz == "" or unit == "" or w == "":
        print("Please enter some numbers.")
        js.alert("Please enter values on the provided space.")
        return
    
    # if sigma_x == sigma_y or sigma_x == sigma_z or sigma_y == sigma_z:
    #     print("Warning: Two or more stress components are equal. This may indicate special stress conditions.")
    #     js.alert("Warning! Two or more stress components are equal. This may indicate special stress conditions.for more information refer the text books!")
    #     return
    
    sigma_x = float(sigma_x)
    sigma_y = float(sigma_y)
    sigma_z = float(sigma_z)
    tau_xy = float(tau_xy)
    tau_yz = float(tau_yz)
    tau_xz = float(tau_xz)
    unit = str(unit)
    w = float(w)
    

    #rotation about z axis
    𝞱=np.radians(w)

    #directional cosines
    l1=np.cos(𝜃)
    m1=np.cos(np.pi/2-𝜃)
    n1=np.cos(np.pi/2)

    l2=np.cos(np.pi/2+𝜃)
    m2=np.cos(𝜃)
    n2=np.cos(np.pi/2)

    l3=np.cos(np.pi/2)
    m3=np.cos(np.pi/2)
    n3=np.cos(0)

    #getting transformed stress tensor states
    sigma_𝑥1 = sigma_𝑥*l1**2 + sigma_𝑦*m1**2 + sigma_𝑧*n1**2 + 2*(tau_𝑥𝑦*l1*m1 + tau_𝑦𝑧*m1*n1 + tau_𝑥𝑧*l1*n1)
    sigma_𝑦1 = sigma_𝑥*l2**2 + sigma_𝑦*m2**2 + sigma_𝑧*n2**2 + 2*(tau_𝑥𝑦*l2*m2 + tau_𝑦𝑧*m2*n2 + tau_𝑥𝑧*l2*n2)
    sigma_𝑧1 = sigma_𝑥*l3**2 + sigma_𝑦*m3**2 + sigma_𝑧*n3**2 + 2*(tau_𝑥𝑦*l3*m3 + tau_𝑦𝑧*m3*n3 + tau_𝑥𝑧*l3*n3)
    tau_𝑥𝑦1 = sigma_𝑥*l1*l2 + sigma_𝑦*m1*m2 + sigma_𝑧*n1*n2 + tau_𝑥𝑦*(l1*m2 + m1*l2) + tau_𝑦𝑧*(m1*n2 + n1*m2) + tau_𝑥𝑧*(n1*l2 + l1*n2)
    tau_𝑦𝑧1 = sigma_𝑥*l2*l3 + sigma_𝑦*m2*m3 + sigma_𝑧*n2*n3 + tau_𝑥𝑦*(m2*l3 + l2*m3) + tau_𝑦𝑧*(n2*m3 + m2*n3) + tau_𝑥𝑧*(l2*n3 + n2*l3)
    tau_𝑥z1 = sigma_𝑥*l1*l3 + sigma_𝑦*m1*m3 + sigma_𝑧*n1*n3 + tau_𝑥𝑦*(l1*m3 + m1*l3) + tau_𝑦𝑧*(m1*n3 + n1*m3) + tau_𝑥𝑧*(n1*l3 + l1*n3)

    𝜏𝑖𝑗_1=np.array([[sigma_𝑥1,tau_𝑥𝑦1,tau_𝑥z1],[tau_𝑥𝑦1,sigma_y1,tau_yz1],[tau_𝑥z1,tau_yz1,sigma_z1]])

    #stress invariants relative to the new coordinate system
    I1=sigma_x1+sigma_y1+sigma_z1
    I2=sigma_x1*sigma_y1+sigma_x1*sigma_z1+sigma_y1*sigma_z1-tau_xy1**2-tau_yz1**2-tau_xz1**2
    I3=np.linalg.det(𝜏𝑖𝑗_1)


    document.querySelector("#outputOne").innerText = f"{round(I1,2)} {unit}"
    document.querySelector("#outputwo").innerText = f"{round(I2,2)} {unit}²"
    document.querySelector("#outputhree").innerText = f"{round(I3,2)} {unit}³"

    document.querySelector("#stress_title").innerText = "'Transformed Stress_Tensor'"
    document.querySelector("#stress_xx").innerText = "σx'"
    document.querySelector("#stress_xy1").innerText = "τx'y'"
    document.querySelector("#stress_xz1").innerText = "τx'z'"
    document.querySelector("#stress_yx2").innerText = "τx'y'"
    document.querySelector("#stress_yy").innerText = "σy'"
    document.querySelector("#stress_yz2").innerText = "τy'z'"
    document.querySelector("#stress_zx3").innerText = "τx'z'"
    document.querySelector("#stress_zy3").innerText = "τy'z'"
    document.querySelector("#stress_zz").innerText = "σz'"

    document.querySelector("#stress_x").innerText = f"{round(sigma_𝑥1,2)} {unit}"
    document.querySelector("#stress_xy").innerText = f"{round(tau_𝑥𝑦1,2)} {unit}"
    document.querySelector("#stress_xz").innerText = f"{round(tau_𝑥z1,2)} {unit}"
    document.querySelector("#stress_yx").innerText = f"{round(tau_𝑥𝑦1,2)} {unit}"
    document.querySelector("#stress_y").innerText = f"{round(sigma_y1,2)} {unit}"
    document.querySelector("#stress_yz").innerText = f"{round(tau_𝑦z1,2)} {unit}"
    document.querySelector("#stress_zx").innerText = f"{round(tau_𝑥z1,2)} {unit}"
    document.querySelector("#stress_zy").innerText = f"{round(tau_𝑦z1,2)} {unit}"
    document.querySelector("#stress_z").innerText = f"{round(sigma_z1,2)} {unit}"

    document.querySelector("#Cosines_title").innerText = "'Directional Cosines'"
    document.querySelector("#l11").innerText = "l1"
    document.querySelector("#m11").innerText = "m1"
    document.querySelector("#n11").innerText = "n1"
    document.querySelector("#l22").innerText = "l2"
    document.querySelector("#m22").innerText = "m2"
    document.querySelector("#n22").innerText = "n2"
    document.querySelector("#l33").innerText = "l3"
    document.querySelector("#m33").innerText = "m3"
    document.querySelector("#n33").innerText = "n3"

    document.querySelector("#l1").innerText = f"{round(l1,3)}"
    document.querySelector("#m1").innerText = f"{round(m1,3)}"
    document.querySelector("#n1").innerText = f"{round(n1,3)}"
    document.querySelector("#l2").innerText = f"{round(l2,3)}"
    document.querySelector("#m2").innerText = f"{round(m2,3)}"
    document.querySelector("#n2").innerText = f"{round(n2,3)}"
    document.querySelector("#l3").innerText = f"{round(l3,3)}"
    document.querySelector("#m3").innerText = f"{round(m3,3)}"
    document.querySelector("#n3").innerText = f"{round(n3,3)}"
    

def clear(*args, **kwargs):
    document.querySelector("#sigma_x").value = ""
    document.querySelector("#sigma_y").value = ""
    document.querySelector("#sigma_z").value = ""
    document.querySelector("#tau_xy").value = ""
    document.querySelector("#tau_xz").value = ""
    document.querySelector("#tau_yz").value = ""
    document.querySelector("#unit").value = ""
    document.querySelector("#w").value = ""
    
    document.querySelector("#outputOne").innerText = ""
    document.querySelector("#outputwo").innerText = ""
    document.querySelector("#outputhree").innerText = ""

    document.querySelector("#stress_title").innerText = ""
    document.querySelector("#stress_xx").innerText = ""
    document.querySelector("#stress_xy1").innerText = ""
    document.querySelector("#stress_xz1").innerText = ""
    document.querySelector("#stress_yx2").innerText = ""
    document.querySelector("#stress_yy").innerText = ""
    document.querySelector("#stress_yz2").innerText = ""
    document.querySelector("#stress_zx3").innerText = ""
    document.querySelector("#stress_zy3").innerText = ""
    document.querySelector("#stress_zz").innerText = ""
    document.querySelector("#stress_x").innerText = ""
    document.querySelector("#stress_xy").innerText = ""
    document.querySelector("#stress_xz").innerText = ""
    document.querySelector("#stress_yx").innerText = ""
    document.querySelector("#stress_y").innerText = ""
    document.querySelector("#stress_yz").innerText = ""
    document.querySelector("#stress_zx").innerText = ""
    document.querySelector("#stress_zy").innerText = ""
    document.querySelector("#stress_z").innerText = ""

    document.querySelector("#Cosines_title").innerText = ""
    document.querySelector("#l11").innerText = ""
    document.querySelector("#m11").innerText = ""
    document.querySelector("#n11").innerText = ""
    document.querySelector("#l22").innerText = ""
    document.querySelector("#m22").innerText = ""
    document.querySelector("#n22").innerText = ""
    document.querySelector("#l33").innerText = ""
    document.querySelector("#m33").innerText = ""
    document.querySelector("#n33").innerText = ""
    document.querySelector("#l1").innerText = ""
    document.querySelector("#m1").innerText = ""
    document.querySelector("#n1").innerText = ""
    document.querySelector("#l2").innerText = ""
    document.querySelector("#m2").innerText = ""
    document.querySelector("#n2").innerText = ""
    document.querySelector("#l3").innerText = ""
    document.querySelector("#m3").innerText = ""
    document.querySelector("#n3").innerText = ""