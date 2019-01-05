from operator import itemgetter

profiles_list = list()
profiles_dict = dict()

with open('m04_lab_profiles','r') as profiles_file:

    for profile_line in profiles_file:

        profile = dict()

        profile_info = profile_line.strip().split(',')

        profile['name'] = profile_info[0]
        profile['location'] = profile_info[1]
        profile['status'] = profile_info[2]
        profile['employer'] = profile_info[3]
        profile['job'] = profile_info[4]

        profiles_dict[profile_info[0]] = profile
        profiles_list.append(profile)

print(profile)


