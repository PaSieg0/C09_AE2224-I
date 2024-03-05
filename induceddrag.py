from aerocoeff import aircraft2global

# Prandtl's lifting line theory says that the induced drag is given by: CDi = CL^2/(pi*AR*e)

# The other way to calculate it from the data is by projectig the lift onto the effective 
# downwash line through the effective angle of attack. Assuming no downwash alpha_eff = alpha