dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}

print("dic1", dic1)
print("dic2", dic2)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}

print("Copiando contenido de dic1 en nuevo_dic")
nuevo_dic = dic1.copy()  # Para evitar modificar dic1 directamente
print("Contenido de nuevo_dic", nuevo_dic)

print("Actualizando Contenido de dic2 en nuevo_dic")
nuevo_dic.update(dic2)
print("Contenido de nuevo_dic", nuevo_dic)

#print(nuevo_dic)


#Clase que recibe los diccionarios como una lista de diccionarios y returna el diccionario definitivo mergeado
class Solution:
    def merge_dictionaries(self, dicts: list[dict[int, int]]) -> dict[int, int]:
        merged_dicts = {}
        for dict in dicts:
            merged_dicts.update(dict)
        return merged_dicts
    
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dictionary_list = [dic1, dic2, dic3]

solution = Solution()
final_result = solution.merge_dictionaries(dictionary_list)
print("Solution Class Result: ", final_result)