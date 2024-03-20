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

    if sigma_x == "" or sigma_y == "" or sigma_z == "" or tau_xy == "" or tau_yz == "" or tau_xz == "" or unit == "":
        print("Please enter some numbers.")
        js.alert("Please enter values on the provided space.")
        return
    
    if sigma_x == sigma_y or sigma_x == sigma_z or sigma_y == sigma_z:
        print("Warning: Two or more stress components are equal. This may indicate special stress conditions.")
        js.alert("Warning! Two or more stress components are equal. This may indicate special stress conditions. for instance, When one of the principal stresses is equal to another, it indicates symmetry in stress distribution along specific axes.")
        return
    
    sigma_x = float(sigma_x)
    sigma_y = float(sigma_y)
    sigma_z = float(sigma_z)
    tau_xy = float(tau_xy)
    tau_yz = float(tau_yz)
    tau_xz = float(tau_xz)
    unit = str(unit)
    

    
    # Rearranging the input tensor
    stress_tensor =[
        [sigma_x,tau_xy,tau_xz],
        [tau_xy,sigma_y,tau_yz],
        [tau_xz,tau_yz,sigma_z]
                    ]
    


    # stress invariants
    I1=sigma_x+sigma_y+sigma_z
    I2=sigma_x*sigma_y+sigma_x*sigma_z+sigma_y*sigma_z-tau_xy**2-tau_yz**2-tau_xz**2
    I3=np.linalg.det(stress_tensor)


    # roots of the polynomial
    equation1= [1, -I1, I2, -I3]
    roots = sorted(np.roots(equation1))
    sigma_1 = roots[2]
    sigma_2 = roots[1]
    sigma_3 = roots[0]

    tau13 = (sigma_1 - sigma_3)/2
    x3 = (sigma_1 + sigma_3)/2

    tau23 = (sigma_2 - sigma_3)/2
    x2 = (sigma_2 + sigma_3)/2

    tau12 = (sigma_1 - sigma_2)/2
    x1 = (sigma_1 + sigma_2)/2

    R = (sigma_1 - sigma_3)/2

    x4, y4 = [x1, x1], [0, tau12]
    x5, y5 = [x2, x2], [0, tau23]
    x6, y6 = [x3, x3], [0, tau13]


    #principal angle
    theta_p = np.degrees(0.5 * np.arctan(2 * tau_xy/(sigma_x - sigma_y)))


    circle_1= plt.Circle((x3,0), tau13, facecolor="grey", edgecolor='r')
    circle_2= plt.Circle((x2,0), tau23, facecolor="purple", edgecolor='b')
    circle_3= plt.Circle((x1,0), tau12, facecolor='orange', edgecolor='g')

    #plotting the circles

    # Create a figure and an axes object
    fig, ax = plt.subplots()

    # Set axis limits
    ax.set_xlim(sigma_3 - 0.5 * tau13, sigma_1 + 0.5 * tau13)
    ax.set_ylim(-1.5 * tau13, 1.7 * tau13)

    # Add patches to the axes
    ax.add_patch(circle_1)
    ax.add_patch(circle_2)
    ax.add_patch(circle_3)

    # Plot lines and markers
    ax.plot(x4, y4, marker='o', color='g')
    ax.plot(x5, y5, marker='o', color='b')
    ax.plot(x6, y6, marker='o', color='r')
    ax.plot([sigma_3 - 10, sigma_1 + 10], [0, 0], linestyle='--', color='black')
    ax.plot([0, 0], [-tau13 - 10, tau13 + 10], linestyle='--', color='black')

    # Add text annotations
    ax.text(x3, tau13 + 0.7, "τ13")
    ax.text(x1, tau12 + 0.7, "τ12")
    ax.text(x2, tau23 + 0.7, "τ23")

    # Set labels and title
    ax.set_xlabel("Normal Stress")
    ax.set_ylabel("Shear Stress")
    ax.set_title("3D Mohr's Circle")

    # Show the plot
    display(fig, target="output")
    
    
    document.querySelector("#outputOne").innerText = f"{round(sigma_1,2)} {unit}"
    document.querySelector("#outputwo").innerText = f"{round(sigma_2,2)} {unit}"
    document.querySelector("#outputhree").innerText = f"{round(sigma_3,2)} {unit}"
    document.querySelector("#outputFour").innerText = f"{round(tau13,2)} {unit}"
    document.querySelector("#outputFive").innerText = f"{round(R,2)} mm"
    document.querySelector("#outputSix").innerText = f"{round(theta_p,2)}°"

    


def clear(*args, **kwargs):
    document.querySelector("#sigma_x").value = ""
    document.querySelector("#sigma_y").value = ""
    document.querySelector("#sigma_z").value = ""
    document.querySelector("#tau_xy").value = ""
    document.querySelector("#tau_xz").value = ""
    document.querySelector("#tau_yz").value = ""
    document.querySelector("#unit").value = ""
    
    document.querySelector("#output").innerText = ""
    document.querySelector("#outputOne").innerText = ""
    document.querySelector("#outputwo").innerText = ""
    document.querySelector("#outputhree").innerText = ""
    document.querySelector("#outputFour").innerText = ""
    document.querySelector("#outputFive").innerText = ""
    document.querySelector("#outputSix").innerText = ""