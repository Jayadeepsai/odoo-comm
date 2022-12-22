{
    'name': "Travel Management",
    'version': '1.1',
    'sequence':30,
    'depends': ['base' , 'mail', 'uom'],
    'author': "Deepu",
    'category': 'management',
    'description': """ Plugin """,
    # data files always loaded at installation
     'data': [
        'security/ir.model.access.csv',
         'views/travel.xml'
     ],
    # # data files containing optionally loaded demonstration data
     'demo': [
    #     'demo/demo_estate_data.xml',
     ],

    'application' : True,
    'installation': True,
    'license':'LGPL-3',
}