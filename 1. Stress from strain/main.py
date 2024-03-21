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
    E = document.querySelector("#E").value
    v = document.querySelector("#v").value

    if sigma_x == "" or sigma_y == "" or sigma_z == "" or tau_xy == "" or tau_yz == "" or tau_xz == "" or E == "" or v == "":
        print("Please enter some numbers.")
        js.alert("Please enter values on the provided space.")
        return
    
    # if sigma_x == sigma_y or sigma_x == sigma_z or sigma_y == sigma_z:
    #     print("Warning: Two or more stress components are equal. This may indicate special stress conditions.")
    #     js.alert("Warning! Two or more stress components are equal. This may indicate special stress conditions. for more information refer the text books!")
    #     return
    
    sigma_x = float(sigma_x)
    sigma_y = float(sigma_y)
    sigma_z = float(sigma_z)
    tau_xy = float(tau_xy)
    tau_yz = float(tau_yz)
    tau_xz = float(tau_xz)
    E = float(E)
    v = float(v)

    
    d = 1/E # inverse of Young's modulus
    
    x = [
    [d, -v*d, -v*d, 0, 0, 0],
    [-v*d, d, -v*d, 0, 0, 0],
    [-v*d, -v*d, d, 0, 0, 0],
    [0, 0, 0, 2*(1+v)*d, 0, 0],
    [0, 0, 0, 0, 2*(1+v)*d, 0],
    [0, 0, 0, 0, 0, 2*(1+v)*d]
    ]
    
    
    y = [
    [sigma_x],
    [sigma_y],
    [sigma_z],
    [tau_xy],
    [tau_yz],
    [tau_xz]
    ]
    
    result = [
    [0],
    [0],
    [0],
    [0],
    [0],
    [0]
    ]
    
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]
    
    
    document.querySelector("#outputOne").innerText = round(result[0][0],2)
    document.querySelector("#outputwo").innerText = round(result[1][0],2)
    document.querySelector("#outputhree").innerText = round(result[2][0],2)
    document.querySelector("#outputFour").innerText = round(result[3][0],2)
    document.querySelector("#outputFive").innerText = round(result[4][0],2)
    document.querySelector("#outputSix").innerText = round(result[5][0],2)


def clear(*args, **kwargs):
    document.querySelector("#sigma_x").value = ""
    document.querySelector("#sigma_y").value = ""
    document.querySelector("#sigma_z").value = ""
    document.querySelector("#tau_xy").value = ""
    document.querySelector("#tau_xz").value = ""
    document.querySelector("#tau_yz").value = ""
    document.querySelector("#E").value = ""
    document.querySelector("#v").value = ""

    document.querySelector("#outputOne").innerText = ""
    document.querySelector("#outputwo").innerText = ""
    document.querySelector("#outputhree").innerText = ""
    document.querySelector("#outputFour").innerText = ""
    document.querySelector("#outputFive").innerText = ""
    document.querySelector("#outputSix").innerText = ""