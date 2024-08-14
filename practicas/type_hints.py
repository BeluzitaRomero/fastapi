# ---------------------------------------------------------------------------- #
#         type hints: me dejan asignarle el tipo a una variable (>3.6v)        #
# ---------------------------------------------------------------------------- #
# Le puedo sugerir que tipo de dato tendra, pero no puedo forzarla.

my_typed_variable: str = "My typed string variable" #aca, por mas que le ponga "int"
#si guarde un string, seguira siendo string

#las sugerencias cuando utilizo la varianle cuando hago "my_type_varianle." si esta en srt
#mostrara opciones de str. So lo configuro en int, mostrara de strings


print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))