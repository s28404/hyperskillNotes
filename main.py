# import matplotlib.pyplot as plt

# # data = [163, 163, 164, 170, 170, 172, 173, 190]
# # plt.hist(data, color="orange", edgecolor="white")
# # plt.title("My friends' height")
# # plt.ylabel("Number of people")
# # plt.xlabel("Height in cm")
# # plt.show()

# # bins = [160, 170, 180, 190]
# # plt.hist(data, color='orange', edgecolor='white', range=(170, 180))

# # plt.legend()
# # plt.show()

# # my_data = [163, 163, 164, 170, 170, 172, 173, 190]
# # andy_data = [161, 172, 174, 175, 181, 183, 186, 190]
# # bins = [160, 170, 180, 190]
# # names = ["my friends", "Andy's friends"]

# # plt.hist([my_data, andy_data], bins=bins, label=names, color=['red', 'green'], stacked=True, edgecolor='white')
# # plt.title("Mine and Andy's friends' height")
# # plt.ylabel("Number of people")
# # plt.xlabel("Height in cm")

# # plt.legend()

# # plt.show()

# # data = [55, 27, 15, 3]
# # labels = ['Chocolate', 'Vanilla', 'Strawberry', 'Other']

# # plt.figure(figsize=(9, 7))
# # explode = [0.0, 0.08, 0.0, 0.0]
# # colors = ['saddlebrown', 'wheat', 'crimson', 'lightgrey']
# # plt.pie(data, 
# #         explode=explode, 
# #         labels=labels,
# #         colors=colors,
# #         autopct='%.1f%%',  # here we also add the % sign
# #         shadow=True)
# # plt.title('The results of the icecream survey', fontsize=14)
# # plt.legend(labels)
# # plt.show()

# # fig, axes = plt.subplots(1, 2, figsize=(10, 6))
# # ax1, ax2 = axes

# # ax1.pie(data, 
# #         labels=labels, 
# #         colors=colors, 
# #         startangle=90,
# #         wedgeprops={'width': 0.2})
# # ax2.pie(data, labels=labels, colors=colors, startangle=90, counterclock=False)
# # ax1.set_title('Starting the plot at 90')
# # ax2.set_title('Plotting clockwise')

# # plt.show()

# # fig, ax = plt.subplots(figsize=(8, 6))
# # width = 0.3

# # icecream_data = [55, 27, 15, 3]
# # icecream_labels = ['Chocolate', 'Vanilla', 'Strawberry', 'Other']
# # icecream_colors = ['saddlebrown', 'wheat', 'crimson', 'lightgrey']

# # icecream_pie = ax.pie(
# #     icecream_data,
# #     radius=1,
# #     labels=icecream_labels,
# #     colors=icecream_colors,
# #     wedgeprops={'width': width},
# # )


# # pets_data = [45, 41, 10, 4]
# # pets_labels = ['Dogs', 'Cats', 'Parrots', 'Other']
# # pets_colors = ['orange', 'teal', 'powderblue', 'grey']
# # pets_pie = ax.pie(
# #     pets_data,
# #     radius=1 - width,
# #     labels=pets_labels,
# #     labeldistance=0.7,
# #     colors=pets_colors,
# #     wedgeprops={'width': width},
# # )

# # plt.show()

# from sklearn.datasets import load_wine
# from sklearn.model_selection import train_test_split

# data = load_wine(as_frame=True)["frame"]
# X, y = data.iloc[:, :-1], data["target"]

# # X_train, X_tests, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)
# X_train, X_tests, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)

# #.fit(), .fit_transform(), and .transform() are the methods of the estimator API in sklearn. The estimator is .fit() only on the train set, while .transform() could be applied to both the training and the test sets. .fit_transform() is the optimized combination of the two methods, equivalent to fit(X_train).transform(X_train).
print("lala")