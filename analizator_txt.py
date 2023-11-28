"""
We analyze the text for the presence of the required laboratory competence
https://bsca.by/ru/registry-testlab/all?RegistryOOSSearch%5Bstate_id%5D=1&RegistryOOSSearch%5Bcertificate_number%5D=&RegistryOOSSearch%5Boos_ul_name%5D=&RegistryOOSSearch%5Bcertificate_reg_date_first%5D=&RegistryOOSSearch%5Borgan_period%5D=&RegistryOOSSearch%5Btc%5D=&page=1
"""

# Input required competencies
competencies = []
while True:
    competence = input("Введите компетенцию: ")
    print(competence)
    if competence == 'end':
        break
    competencies.append(competence)
print(competencies)

# List of all laboratory competencies
list_competencies = "Оборудование, работающее под избыточным давлением: -сосуды и аппараты, работающие под давлением; -паровые и водогрейные котлы. - трубопроводы пара и горячей воды. Грузоподъемное оборудование: - грузоподъемные краны - грузозахватные органы - тара. Объекты литейного производства. Образцы сварных соединений для аттестации сварщиков. Образцы сварных соединений для аттестации сварщиков. Чугунное литье. Цветное литье. Стальное литье. Входной контроль стального металлопроката. Крепежные изделия. Трубы. Проволока стальная. Прутки стальные. Прокат стальной (листы, ленты). Листы и ленты из цветных металлов. Тентовый материал. Детали МАЗ. Детали, подвергаемые химико-термической обработке. Детали, подвергаемые закалке ТВЧ. Детали, подвергаемые улучшению. Детали МАЗ входной контроль стального металлопроката."

answer = False
for c in competencies:
    if list_competencies.lower().find(c) != -1:
        answer = True
        break
    else:
        print(False)
print(answer)
