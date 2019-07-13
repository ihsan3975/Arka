import json
class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)
my_identities = {"name":'Maulana Ihsan',
                'age': 22,
                'address': 'Jalan Idris, Jakbar',
                'hobbies': ['Tidur', 'Jalan-jalan'],
                'is_married': False,
                'list_school': [{'year_in : 2003, year_out : 2009, major : null'},
                                {'year_in : 2009, year_out : 2012, major : null'},
                                {'year_in : 2012, year_out : 2015, major : Science'},
                                {'year_in : 2015, year_out : 2019, major : Physics'}],
                 'skills' : [{'skill name : python, level : beginner'},
                             {'skill name : matlab, level : beginner'},
                             {'skill name : machine learning, level : beginner'}],
                 'interest_in_coding': True
                }
print(json.dumps(my_identities, cls=SetEncoder))