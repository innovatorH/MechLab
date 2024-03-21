# importing the neccessary modules
from pyscript import document
from pyscript import display
import matplotlib.pyplot as plt
import numpy as np
import js


def calculate(*args, **kwargs):

    strain_x = document.querySelector("#strain_x").value
    strain_y = document.querySelector("#strain_y").value
    strain_z = document.querySelector("#strain_z").value
    gamma_xy = document.querySelector("#gamma_xy").value
    gamma_yz = document.querySelector("#gamma_yz").value
    gamma_xz = document.querySelector("#gamma_xz").value
    E = document.querySelector("#E").value
    v = document.querySelector("#v").value

    if strain_x == "" or strain_y == "" or strain_z == "" or gamma_xy == "" or gamma_yz == "" or gamma_xz == "" or E == "" or v == "":
        print("Please enter some numbers.")
        js.alert("Please enter values on the provided space.")
        return
    
    # Check if any two input values are equal
    # if strain_x == strain_y or strain_x == strain_z or strain_y == strain_z \
    #         or gamma_xy == gamma_yz or gamma_xy == gamma_xz or gamma_yz == gamma_xz:
    #     print("Warning: Two or more strain or shear components are equal. This may indicate special conditions.")
    #     js.alert("Warning! Two or more strain or shear components are equal. This may indicate special conditions. for more information refer the text books!")
    #     return

    strain_x = float(strain_x)
    strain_y = float(strain_y)
    strain_z = float(strain_z)
    gamma_xy = float(gamma_xy)
    gamma_yz = float(gamma_yz)
    gamma_xz = float(gamma_xz)
    E = float(E)
    v = float(v)

    
    c = E/((1+v)*(1-2*v))


    x = [
        [c*(1-v),c*v,c*v,0,0,0],
        [c*v,c*(1-v),c*v,0 ,0,0],
        [c*v,c*v,c*(1-v) ,0,0,0],
        [0,0,0,c*(0.5-1*v),0,0],
        [0,0,0,0,c*(0.5-1*v),0],
        [0,0,0,0,0,c*(0.5-1*v)]
    ]
 
    y = [
        [strain_x],
        [strain_y],
        [strain_z],
        [gamma_yz],
        [gamma_xz],
        [gamma_xy]
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
    
    
    document.querySelector("#outputOne").innerText = (round(result[0][0],5))
    document.querySelector("#outputwo").innerText = (round(result[1][0],5))
    document.querySelector("#outputhree").innerText = (round(result[2][0],5))
    document.querySelector("#outputFour").innerText = (round(result[3][0],5))
    document.querySelector("#outputFive").innerText = (round(result[4][0],5))
    document.querySelector("#outputSix").innerText = (round(result[5][0],5))


def clear(*args, **kwargs):
    document.querySelector("#strain_x").value = ""
    document.querySelector("#strain_y").value = ""
    document.querySelector("#strain_z").value = ""
    document.querySelector("#gamma_xy").value = ""
    document.querySelector("#gamma_xz").value = ""
    document.querySelector("#gamma_yz").value = ""
    document.querySelector("#E").value = ""
    document.querySelector("#v").value = ""

    document.querySelector("#outputOne").innerText = ""
    document.querySelector("#outputwo").innerText = ""
    document.querySelector("#outputhree").innerText = ""
    document.querySelector("#outputFour").innerText = ""
    document.querySelector("#outputFive").innerText = ""
    document.querySelector("#outputSix").innerText = ""