DATASET_BASE = '/mnt/LIVELAB_NAS/Detecting-AI-Generated-Images/UnivFD/dataset/val/'
DATASET_PATHS = [


    dict(
        real_path=DATASET_BASE+'progan',     
        fake_path=DATASET_BASE+'progan',
        data_mode='wang2020',
        key='progan'
    ),

    dict(
        real_path=DATASET_BASE+'cyclegan',   
        fake_path=DATASET_BASE+'cyclegan',
        data_mode='wang2020',
        key='cyclegan'
    ),

    dict(
        real_path=DATASET_BASE+'biggan/',   # Imagenet 
        fake_path=DATASET_BASE+'biggan/',
        data_mode='wang2020',
        key='biggan'
    ),


    dict(
        real_path=DATASET_BASE+'stylegan',    
        fake_path=DATASET_BASE+'stylegan',
        data_mode='wang2020',
        key='stylegan'
    ),


    dict(
        real_path=DATASET_BASE+'gaugan',    # It is COCO 
        fake_path=DATASET_BASE+'gaugan',
        data_mode='wang2020',
        key='gaugan'
    ),


    dict(
        real_path=DATASET_BASE+'stargan',  
        fake_path=DATASET_BASE+'stargan',
        data_mode='wang2020',
        key='stargan'
    ),


    dict(
        real_path=DATASET_BASE+'deepfake',   
        fake_path=DATASET_BASE+'deepfake',
        data_mode='wang2020',
        key='deepfake'
    ),


    dict(
        real_path=DATASET_BASE+'seeingdark',   
        fake_path=DATASET_BASE+'seeingdark',
        data_mode='wang2020',
        key='sitd'
    ),


    dict(
        real_path=DATASET_BASE+'san',   
        fake_path=DATASET_BASE+'san',
        data_mode='wang2020',
        key='san'
    ),


    dict(
        real_path=DATASET_BASE+'crn',   # Images from some video games
        fake_path=DATASET_BASE+'crn',
        data_mode='wang2020',
        key='crn'
    ),


    dict(
        real_path=DATASET_BASE+'imle',   # Images from some video games
        fake_path=DATASET_BASE+'imle',
        data_mode='wang2020',
        key='imle'
    ),
    

    dict(
        real_path=DATASET_BASE+'imagenet',
        fake_path=DATASET_BASE+'guided',
        data_mode='wang2020',
        key='guided'
    ),


    dict(
        real_path=DATASET_BASE+'laion',
        fake_path=DATASET_BASE+'ldm_200',
        data_mode='wang2020',
        key='ldm_200'
    ),

    dict(
        real_path=DATASET_BASE+'laion',
        fake_path=DATASET_BASE+'ldm_200_cfg',
        data_mode='wang2020',
        key='ldm_200_cfg'
    ),

    dict(
        real_path=DATASET_BASE+'laion',
        fake_path=DATASET_BASE+'ldm_100',
        data_mode='wang2020',
        key='ldm_100'
     ),


    dict(
        real_path=DATASET_BASE+'laion',
        fake_path=DATASET_BASE+'glide_100_27',
        data_mode='wang2020',
        key='glide_100_27'
    ),


    dict(
        real_path=DATASET_BASE+'laion',
        fake_path=DATASET_BASE+'glide_50_27',
        data_mode='wang2020',
        key='glide_50_27'
    ),


    dict(
        real_path=DATASET_BASE+'laion',
        fake_path=DATASET_BASE+'glide_100_10',
        data_mode='wang2020',
        key='glide_100_10'
    ),


    dict(
        real_path=DATASET_BASE+'laion',
        fake_path=DATASET_BASE+'dalle',
        data_mode='wang2020',
        key='dalle'
    ),



]

# DATASET_BASE = '/mnt/LIVELAB_NAS/Detecting-AI-Generated-Images/GenImage/dataset/'

# DATASET_PATHS = [

#     dict(
#         real_path=DATASET_BASE+'midjourney/val/nature',     
#         fake_path=DATASET_BASE+'midjourney/val/ai',
#         data_mode='ours',
#         key='midjourney'
#     ),

#     dict(
#         real_path=DATASET_BASE+'sdv4/val/nature',     
#         fake_path=DATASET_BASE+'sdv4/val/ai',
#         data_mode='ours',
#         key='sdv4'
#     ),

#     dict(
#         real_path=DATASET_BASE+'sdv5/val/nature',     
#         fake_path=DATASET_BASE+'sdv5/val/ai',
#         data_mode='ours',
#         key='sdv5'
#     ),

#     dict(
#         real_path=DATASET_BASE+'adm/val/nature',     
#         fake_path=DATASET_BASE+'adm/val/ai',
#         data_mode='ours',
#         key='adm'
#     ),

#     dict(
#         real_path=DATASET_BASE+'glide/val/nature',     
#         fake_path=DATASET_BASE+'glide/val/ai',
#         data_mode='ours',
#         key='glide'
#     ),

#     dict(
#         real_path=DATASET_BASE+'wukong/val/nature',     
#         fake_path=DATASET_BASE+'wukong/val/ai',
#         data_mode='ours',
#         key='wukong'
#     ),

#     dict(
#         real_path=DATASET_BASE+'vqdm/val/nature',     
#         fake_path=DATASET_BASE+'vqdm/val/ai',
#         data_mode='ours',
#         key='vqdm'
#     ),

#     dict(
#         real_path=DATASET_BASE+'biggan/val/nature',     
#         fake_path=DATASET_BASE+'biggan/val/ai',
#         data_mode='ours',
#         key='biggan'
#     ),
# ]
