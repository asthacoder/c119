import pandas as pd

#Column Name
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']

df = pd.read_csv("titanic.csv", names=col_names).iloc[1:]

print(df.head())

features = ['pregnant', 'insulin', 'bmi', 'age','glucose','bp','pedigree']
X = df[features]
y = df.label

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

#splitting data in training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

#Initialising the Decision Tree Model
clf = DecisionTreeClassifier()

#Fitting the data into the model
clf = clf.fit(X_train,y_train)

#Calculating the accuracy of the model
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


digraph Tree {
node [shape=box, style="filled, rounded", color="black", fontname=helvetica] ;
edge [fontname=helvetica] ;
0 [label=<glucose &le; 129.5<br/>gini = 0.449<br/>samples = 537<br/>value = [354, 183]<br/>class = 0>, fillcolor="#f2c29f"] ;
1 [label=<bmi &le; 26.3<br/>gini = 0.329<br/>samples = 357<br/>value = [283, 74]<br/>class = 0>, fillcolor="#eca26d"] ;
0 -> 1 [labeldistance=2.5, labelangle=45, headlabel="True"] ;
2 [label=<bmi &le; 9.1<br/>gini = 0.06<br/>samples = 97<br/>value = [94, 3]<br/>class = 0>, fillcolor="#e6853f"] ;
1 -> 2 ;
3 [label=<age &le; 28.0<br/>gini = 0.444<br/>samples = 6<br/>value = [4, 2]<br/>class = 0>, fillcolor="#f2c09c"] ;
2 -> 3 ;
4 [label=<gini = 0.0<br/>samples = 4<br/>value = [4, 0]<br/>class = 0>, fillcolor="#e58139"] ;
3 -> 4 ;
5 [label=<gini = 0.0<br/>samples = 2<br/>value = [0, 2]<br/>class = 1>, fillcolor="#399de5"] ;
3 -> 5 ;
6 [label=<pedigree &le; 0.669<br/>gini = 0.022<br/>samples = 91<br/>value = [90, 1]<br/>class = 0>, fillcolor="#e5823b"] ;
2 -> 6 ;
7 [label=<gini = 0.0<br/>samples = 76<br/>value = [76, 0]<br/>class = 0>, fillcolor="#e58139"] ;
6 -> 7 ;
8 [label=<pedigree &le; 0.705<br/>gini = 0.124<br/>samples = 15<br/>value = [14, 1]<br/>class = 0>, fillcolor="#e78a47"] ;
6 -> 8 ;
9 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
8 -> 9 ;
10 [label=<gini = 0.0<br/>samples = 14<br/>value = [14, 0]<br/>class = 0>, fillcolor="#e58139"] ;
8 -> 10 ;
11 [label=<age &le; 27.5<br/>gini = 0.397<br/>samples = 260<br/>value = [189, 71]<br/>class = 0>, fillcolor="#efb083"] ;
1 -> 11 ;
12 [label=<bmi &le; 45.4<br/>gini = 0.243<br/>samples = 120<br/>value = [103, 17]<br/>class = 0>, fillcolor="#e9965a"] ;
11 -> 12 ;
13 [label=<bp &le; 12.0<br/>gini = 0.212<br/>samples = 116<br/>value = [102, 14]<br/>class = 0>, fillcolor="#e99254"] ;
12 -> 13 ;
14 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
13 -> 14 ;
15 [label=<pregnant &le; 7.0<br/>gini = 0.201<br/>samples = 115<br/>value = [102, 13]<br/>class = 0>, fillcolor="#e89152"] ;
13 -> 15 ;
16 [label=<pedigree &le; 1.272<br/>gini = 0.188<br/>samples = 114<br/>value = [102, 12]<br/>class = 0>, fillcolor="#e89050"] ;
15 -> 16 ;
17 [label=<bmi &le; 30.95<br/>gini = 0.165<br/>samples = 110<br/>value = [100, 10]<br/>class = 0>, fillcolor="#e88e4d"] ;
16 -> 17 ;
18 [label=<gini = 0.0<br/>samples = 43<br/>value = [43, 0]<br/>class = 0>, fillcolor="#e58139"] ;
17 -> 18 ;
19 [label=<bp &le; 53.0<br/>gini = 0.254<br/>samples = 67<br/>value = [57, 10]<br/>class = 0>, fillcolor="#ea975c"] ;
17 -> 19 ;
20 [label=<pregnant &le; 2.5<br/>gini = 0.5<br/>samples = 6<br/>value = [3, 3]<br/>class = 0>, fillcolor="#ffffff"] ;
19 -> 20 ;
21 [label=<insulin &le; 179.5<br/>gini = 0.375<br/>samples = 4<br/>value = [3, 1]<br/>class = 0>, fillcolor="#eeab7b"] ;
20 -> 21 ;
22 [label=<gini = 0.0<br/>samples = 3<br/>value = [3, 0]<br/>class = 0>, fillcolor="#e58139"] ;
21 -> 22 ;
23 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
21 -> 23 ;
24 [label=<gini = 0.0<br/>samples = 2<br/>value = [0, 2]<br/>class = 1>, fillcolor="#399de5"] ;
20 -> 24 ;
25 [label=<pedigree &le; 0.652<br/>gini = 0.203<br/>samples = 61<br/>value = [54, 7]<br/>class = 0>, fillcolor="#e89153"] ;
19 -> 25 ;
26 [label=<insulin &le; 36.5<br/>gini = 0.15<br/>samples = 49<br/>value = [45, 4]<br/>class = 0>, fillcolor="#e78c4b"] ;
25 -> 26 ;
27 [label=<insulin &le; 34.0<br/>gini = 0.32<br/>samples = 20<br/>value = [16, 4]<br/>class = 0>, fillcolor="#eca06a"] ;
26 -> 27 ;
28 [label=<glucose &le; 111.5<br/>gini = 0.266<br/>samples = 19<br/>value = [16, 3]<br/>class = 0>, fillcolor="#ea995e"] ;
27 -> 28 ;
29 [label=<bmi &le; 37.95<br/>gini = 0.142<br/>samples = 13<br/>value = [12, 1]<br/>class = 0>, fillcolor="#e78c49"] ;
28 -> 29 ;
30 [label=<gini = 0.0<br/>samples = 11<br/>value = [11, 0]<br/>class = 0>, fillcolor="#e58139"] ;
29 -> 30 ;
31 [label=<glucose &le; 94.5<br/>gini = 0.5<br/>samples = 2<br/>value = [1, 1]<br/>class = 0>, fillcolor="#ffffff"] ;
29 -> 31 ;
32 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
31 -> 32 ;
33 [label=<gini = 0.0<br/>samples = 1<br/>value = [1, 0]<br/>class = 0>, fillcolor="#e58139"] ;
31 -> 33 ;
34 [label=<bmi &le; 34.5<br/>gini = 0.444<br/>samples = 6<br/>value = [4, 2]<br/>class = 0>, fillcolor="#f2c09c"] ;
28 -> 34 ;
35 [label=<bp &le; 66.0<br/>gini = 0.444<br/>samples = 3<br/>value = [1, 2]<br/>class = 1>, fillcolor="#9ccef2"] ;
34 -> 35 ;
36 [label=<gini = 0.0<br/>samples = 1<br/>value = [1, 0]<br/>class = 0>, fillcolor="#e58139"] ;
35 -> 36 ;
37 [label=<gini = 0.0<br/>samples = 2<br/>value = [0, 2]<br/>class = 1>, fillcolor="#399de5"] ;
35 -> 37 ;
38 [label=<gini = 0.0<br/>samples = 3<br/>value = [3, 0]<br/>class = 0>, fillcolor="#e58139"] ;
34 -> 38 ;
39 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
27 -> 39 ;
40 [label=<gini = 0.0<br/>samples = 29<br/>value = [29, 0]<br/>class = 0>, fillcolor="#e58139"] ;
26 -> 40 ;
41 [label=<insulin &le; 65.5<br/>gini = 0.375<br/>samples = 12<br/>value = [9, 3]<br/>class = 0>, fillcolor="#eeab7b"] ;
25 -> 41 ;
42 [label=<gini = 0.0<br/>samples = 7<br/>value = [7, 0]<br/>class = 0>, fillcolor="#e58139"] ;
41 -> 42 ;
43 [label=<bmi &le; 38.55<br/>gini = 0.48<br/>samples = 5<br/>value = [2, 3]<br/>class = 1>, fillcolor="#bddef6"] ;
41 -> 43 ;
44 [label=<gini = 0.0<br/>samples = 3<br/>value = [0, 3]<br/>class = 1>, fillcolor="#399de5"] ;
43 -> 44 ;
45 [label=<gini = 0.0<br/>samples = 2<br/>value = [2, 0]<br/>class = 0>, fillcolor="#e58139"] ;
43 -> 45 ;
46 [label=<pedigree &le; 1.496<br/>gini = 0.5<br/>samples = 4<br/>value = [2, 2]<br/>class = 0>, fillcolor="#ffffff"] ;
16 -> 46 ;
47 [label=<gini = 0.0<br/>samples = 2<br/>value = [0, 2]<br/>class = 1>, fillcolor="#399de5"] ;
46 -> 47 ;
48 [label=<gini = 0.0<br/>samples = 2<br/>value = [2, 0]<br/>class = 0>, fillcolor="#e58139"] ;
46 -> 48 ;
49 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
15 -> 49 ;
50 [label=<age &le; 22.5<br/>gini = 0.375<br/>samples = 4<br/>value = [1, 3]<br/>class = 1>, fillcolor="#7bbeee"] ;
12 -> 50 ;
51 [label=<gini = 0.0<br/>samples = 1<br/>value = [1, 0]<br/>class = 0>, fillcolor="#e58139"] ;
50 -> 51 ;
52 [label=<gini = 0.0<br/>samples = 3<br/>value = [0, 3]<br/>class = 1>, fillcolor="#399de5"] ;
50 -> 52 ;
53 [label=<pedigree &le; 0.563<br/>gini = 0.474<br/>samples = 140<br/>value = [86, 54]<br/>class = 0>, fillcolor="#f5d0b5"] ;
11 -> 53 ;
54 [label=<glucose &le; 101.5<br/>gini = 0.408<br/>samples = 98<br/>value = [70, 28]<br/>class = 0>, fillcolor="#efb388"] ;
53 -> 54 ;
55 [label=<bp &le; 27.0<br/>gini = 0.208<br/>samples = 34<br/>value = [30, 4]<br/>class = 0>, fillcolor="#e89253"] ;
54 -> 55 ;
56 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
55 -> 56 ;
57 [label=<age &le; 42.5<br/>gini = 0.165<br/>samples = 33<br/>value = [30, 3]<br/>class = 0>, fillcolor="#e88e4d"] ;
55 -> 57 ;
58 [label=<gini = 0.0<br/>samples = 23<br/>value = [23, 0]<br/>class = 0>, fillcolor="#e58139"] ;
57 -> 58 ;
59 [label=<pedigree &le; 0.383<br/>gini = 0.42<br/>samples = 10<br/>value = [7, 3]<br/>class = 0>, fillcolor="#f0b78e"] ;
57 -> 59 ;
60 [label=<glucose &le; 76.0<br/>gini = 0.5<br/>samples = 6<br/>value = [3, 3]<br/>class = 0>, fillcolor="#ffffff"] ;
59 -> 60 ;
61 [label=<gini = 0.0<br/>samples = 2<br/>value = [2, 0]<br/>class = 0>, fillcolor="#e58139"] ;
60 -> 61 ;
62 [label=<glucose &le; 99.0<br/>gini = 0.375<br/>samples = 4<br/>value = [1, 3]<br/>class = 1>, fillcolor="#7bbeee"] ;
60 -> 62 ;
63 [label=<gini = 0.0<br/>samples = 3<br/>value = [0, 3]<br/>class = 1>, fillcolor="#399de5"] ;
62 -> 63 ;
64 [label=<gini = 0.0<br/>samples = 1<br/>value = [1, 0]<br/>class = 0>, fillcolor="#e58139"] ;
62 -> 64 ;
65 [label=<gini = 0.0<br/>samples = 4<br/>value = [4, 0]<br/>class = 0>, fillcolor="#e58139"] ;
59 -> 65 ;
66 [label=<bp &le; 67.0<br/>gini = 0.469<br/>samples = 64<br/>value = [40, 24]<br/>class = 0>, fillcolor="#f5cdb0"] ;
54 -> 66 ;
67 [label=<bp &le; 58.0<br/>gini = 0.465<br/>samples = 19<br/>value = [7, 12]<br/>class = 1>, fillcolor="#acd6f4"] ;
66 -> 67 ;
68 [label=<bmi &le; 30.05<br/>gini = 0.245<br/>samples = 7<br/>value = [6, 1]<br/>class = 0>, fillcolor="#e9965a"] ;
67 -> 68 ;
69 [label=<pedigree &le; 0.182<br/>gini = 0.5<br/>samples = 2<br/>value = [1, 1]<br/>class = 0>, fillcolor="#ffffff"] ;
68 -> 69 ;
70 [label=<gini = 0.0<br/>samples = 1<br/>value = [1, 0]<br/>class = 0>, fillcolor="#e58139"] ;
69 -> 70 ;
71 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
69 -> 71 ;
72 [label=<gini = 0.0<br/>samples = 5<br/>value = [5, 0]<br/>class = 0>, fillcolor="#e58139"] ;
68 -> 72 ;
73 [label=<pedigree &le; 0.425<br/>gini = 0.153<br/>samples = 12<br/>value = [1, 11]<br/>class = 1>, fillcolor="#4ba6e7"] ;
67 -> 73 ;
74 [label=<gini = 0.0<br/>samples = 11<br/>value = [0, 11]<br/>class = 1>, fillcolor="#399de5"] ;
73 -> 74 ;
75 [label=<gini = 0.0<br/>samples = 1<br/>value = [1, 0]<br/>class = 0>, fillcolor="#e58139"] ;
73 -> 75 ;
76 [label=<bmi &le; 43.1<br/>gini = 0.391<br/>samples = 45<br/>value = [33, 12]<br/>class = 0>, fillcolor="#eeaf81"] ;
66 -> 76 ;
77 [label=<glucose &le; 102.5<br/>gini = 0.337<br/>samples = 42<br/>value = [33, 9]<br/>class = 0>, fillcolor="#eca36f"] ;
76 -> 77 ;
78 [label=<gini = 0.0<br/>samples = 2<br/>value = [0, 2]<br/>class = 1>, fillcolor="#399de5"] ;
77 -> 78 ;
79 [label=<bmi &le; 34.6<br/>gini = 0.289<br/>samples = 40<br/>value = [33, 7]<br/>class = 0>, fillcolor="#eb9c63"] ;
77 -> 79 ;
80 [label=<age &le; 35.0<br/>gini = 0.434<br/>samples = 22<br/>value = [15, 7]<br/>class = 0>, fillcolor="#f1bc95"] ;
79 -> 80 ;
81 [label=<gini = 0.0<br/>samples = 6<br/>value = [6, 0]<br/>class = 0>, fillcolor="#e58139"] ;
80 -> 81 ;
82 [label=<glucose &le; 123.5<br/>gini = 0.492<br/>samples = 16<br/>value = [9, 7]<br/>class = 0>, fillcolor="#f9e3d3"] ;
80 -> 82 ;
83 [label=<pedigree &le; 0.375<br/>gini = 0.426<br/>samples = 13<br/>value = [9, 4]<br/>class = 0>, fillcolor="#f1b991"] ;
82 -> 83 ;
84 [label=<pregnant &le; 6.5<br/>gini = 0.298<br/>samples = 11<br/>value = [9, 2]<br/>class = 0>, fillcolor="#eb9d65"] ;
83 -> 84 ;
85 [label=<bp &le; 85.0<br/>gini = 0.444<br/>samples = 6<br/>value = [4, 2]<br/>class = 0>, fillcolor="#f2c09c"] ;
84 -> 85 ;
86 [label=<pedigree &le; 0.206<br/>gini = 0.444<br/>samples = 3<br/>value = [1, 2]<br/>class = 1>, fillcolor="#9ccef2"] ;
85 -> 86 ;
87 [label=<gini = 0.0<br/>samples = 1<br/>value = [1, 0]<br/>class = 0>, fillcolor="#e58139"] ;
86 -> 87 ;
88 [label=<gini = 0.0<br/>samples = 2<br/>value = [0, 2]<br/>class = 1>, fillcolor="#399de5"] ;
86 -> 88 ;
89 [label=<gini = 0.0<br/>samples = 3<br/>value = [3, 0]<br/>class = 0>, fillcolor="#e58139"] ;
85 -> 89 ;
90 [label=<gini = 0.0<br/>samples = 5<br/>value = [5, 0]<br/>class = 0>, fillcolor="#e58139"] ;
84 -> 90 ;
91 [label=<gini = 0.0<br/>samples = 2<br/>value = [0, 2]<br/>class = 1>, fillcolor="#399de5"] ;
83 -> 91 ;
92 [label=<gini = 0.0<br/>samples = 3<br/>value = [0, 3]<br/>class = 1>, fillcolor="#399de5"] ;
82 -> 92 ;
93 [label=<gini = 0.0<br/>samples = 18<br/>value = [18, 0]<br/>class = 0>, fillcolor="#e58139"] ;
79 -> 93 ;
94 [label=<gini = 0.0<br/>samples = 3<br/>value = [0, 3]<br/>class = 1>, fillcolor="#399de5"] ;
76 -> 94 ;
95 [label=<pregnant &le; 8.5<br/>gini = 0.472<br/>samples = 42<br/>value = [16, 26]<br/>class = 1>, fillcolor="#b3d9f5"] ;
53 -> 95 ;
96 [label=<bp &le; 87.0<br/>gini = 0.5<br/>samples = 33<br/>value = [16, 17]<br/>class = 1>, fillcolor="#f3f9fd"] ;
95 -> 96 ;
97 [label=<glucose &le; 97.0<br/>gini = 0.477<br/>samples = 28<br/>value = [11, 17]<br/>class = 1>, fillcolor="#b9dcf6"] ;
96 -> 97 ;
98 [label=<gini = 0.0<br/>samples = 4<br/>value = [4, 0]<br/>class = 0>, fillcolor="#e58139"] ;
97 -> 98 ;
99 [label=<glucose &le; 116.5<br/>gini = 0.413<br/>samples = 24<br/>value = [7, 17]<br/>class = 1>, fillcolor="#8bc5f0"] ;
97 -> 99 ;
100 [label=<pedigree &le; 1.395<br/>gini = 0.165<br/>samples = 11<br/>value = [1, 10]<br/>class = 1>, fillcolor="#4da7e8"] ;
99 -> 100 ;
101 [label=<gini = 0.0<br/>samples = 10<br/>value = [0, 10]<br/>class = 1>, fillcolor="#399de5"] ;
100 -> 101 ;
102 [label=<gini = 0.0<br/>samples = 1<br/>value = [1, 0]<br/>class = 0>, fillcolor="#e58139"] ;
100 -> 102 ;
103 [label=<insulin &le; 78.0<br/>gini = 0.497<br/>samples = 13<br/>value = [6, 7]<br/>class = 1>, fillcolor="#e3f1fb"] ;
99 -> 103 ;
104 [label=<gini = 0.0<br/>samples = 3<br/>value = [3, 0]<br/>class = 0>, fillcolor="#e58139"] ;
103 -> 104 ;
105 [label=<glucose &le; 123.5<br/>gini = 0.42<br/>samples = 10<br/>value = [3, 7]<br/>class = 1>, fillcolor="#8ec7f0"] ;
103 -> 105 ;
106 [label=<glucose &le; 119.5<br/>gini = 0.5<br/>samples = 6<br/>value = [3, 3]<br/>class = 0>, fillcolor="#ffffff"] ;
105 -> 106 ;
107 [label=<gini = 0.0<br/>samples = 2<br/>value = [0, 2]<br/>class = 1>, fillcolor="#399de5"] ;
106 -> 107 ;
108 [label=<insulin &le; 157.0<br/>gini = 0.375<br/>samples = 4<br/>value = [3, 1]<br/>class = 0>, fillcolor="#eeab7b"] ;
106 -> 108 ;
109 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
108 -> 109 ;
110 [label=<gini = 0.0<br/>samples = 3<br/>value = [3, 0]<br/>class = 0>, fillcolor="#e58139"] ;
108 -> 110 ;
111 [label=<gini = 0.0<br/>samples = 4<br/>value = [0, 4]<br/>class = 1>, fillcolor="#399de5"] ;
105 -> 111 ;
112 [label=<gini = 0.0<br/>samples = 5<br/>value = [5, 0]<br/>class = 0>, fillcolor="#e58139"] ;
96 -> 112 ;
113 [label=<gini = 0.0<br/>samples = 9<br/>value = [0, 9]<br/>class = 1>, fillcolor="#399de5"] ;
95 -> 113 ;
114 [label=<bmi &le; 27.85<br/>gini = 0.478<br/>samples = 180<br/>value = [71, 109]<br/>class = 1>, fillcolor="#baddf6"] ;
0 -> 114 [labeldistance=2.5, labelangle=-45, headlabel="False"] ;
115 [label=<glucose &le; 145.5<br/>gini = 0.375<br/>samples = 36<br/>value = [27, 9]<br/>class = 0>, fillcolor="#eeab7b"] ;
114 -> 115 ;
116 [label=<age &le; 59.5<br/>gini = 0.1<br/>samples = 19<br/>value = [18, 1]<br/>class = 0>, fillcolor="#e68844"] ;
115 -> 116 ;
117 [label=<gini = 0.0<br/>samples = 16<br/>value = [16, 0]<br/>class = 0>, fillcolor="#e58139"] ;
116 -> 117 ;
118 [label=<bmi &le; 25.25<br/>gini = 0.444<br/>samples = 3<br/>value = [2, 1]<br/>class = 0>, fillcolor="#f2c09c"] ;
116 -> 118 ;
119 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
118 -> 119 ;
120 [label=<gini = 0.0<br/>samples = 2<br/>value = [2, 0]<br/>class = 0>, fillcolor="#e58139"] ;
118 -> 120 ;
121 [label=<bmi &le; 23.1<br/>gini = 0.498<br/>samples = 17<br/>value = [9, 8]<br/>class = 0>, fillcolor="#fcf1e9"] ;
115 -> 121 ;
122 [label=<gini = 0.0<br/>samples = 3<br/>value = [3, 0]<br/>class = 0>, fillcolor="#e58139"] ;
121 -> 122 ;
123 [label=<bmi &le; 25.55<br/>gini = 0.49<br/>samples = 14<br/>value = [6, 8]<br/>class = 1>, fillcolor="#cee6f8"] ;
121 -> 123 ;
124 [label=<gini = 0.0<br/>samples = 6<br/>value = [0, 6]<br/>class = 1>, fillcolor="#399de5"] ;
123 -> 124 ;
125 [label=<glucose &le; 156.0<br/>gini = 0.375<br/>samples = 8<br/>value = [6, 2]<br/>class = 0>, fillcolor="#eeab7b"] ;
123 -> 125 ;
126 [label=<gini = 0.0<br/>samples = 2<br/>value = [0, 2]<br/>class = 1>, fillcolor="#399de5"] ;
125 -> 126 ;
127 [label=<gini = 0.0<br/>samples = 6<br/>value = [6, 0]<br/>class = 0>, fillcolor="#e58139"] ;
125 -> 127 ;
128 [label=<glucose &le; 158.5<br/>gini = 0.424<br/>samples = 144<br/>value = [44, 100]<br/>class = 1>, fillcolor="#90c8f0"] ;
114 -> 128 ;
129 [label=<age &le; 30.5<br/>gini = 0.487<br/>samples = 88<br/>value = [37, 51]<br/>class = 1>, fillcolor="#c9e4f8"] ;
128 -> 129 ;
130 [label=<bp &le; 23.0<br/>gini = 0.49<br/>samples = 42<br/>value = [24, 18]<br/>class = 0>, fillcolor="#f8e0ce"] ;
129 -> 130 ;
131 [label=<gini = 0.0<br/>samples = 4<br/>value = [0, 4]<br/>class = 1>, fillcolor="#399de5"] ;
130 -> 131 ;
132 [label=<bp &le; 88.0<br/>gini = 0.465<br/>samples = 38<br/>value = [24, 14]<br/>class = 0>, fillcolor="#f4caac"] ;
130 -> 132 ;
133 [label=<bp &le; 72.0<br/>gini = 0.444<br/>samples = 36<br/>value = [24, 12]<br/>class = 0>, fillcolor="#f2c09c"] ;
132 -> 133 ;
134 [label=<bmi &le; 33.75<br/>gini = 0.5<br/>samples = 20<br/>value = [10, 10]<br/>class = 0>, fillcolor="#ffffff"] ;
133 -> 134 ;
135 [label=<bmi &le; 31.05<br/>gini = 0.397<br/>samples = 11<br/>value = [8, 3]<br/>class = 0>, fillcolor="#efb083"] ;
134 -> 135 ;
136 [label=<bp &le; 58.0<br/>gini = 0.5<br/>samples = 6<br/>value = [3, 3]<br/>class = 0>, fillcolor="#ffffff"] ;
135 -> 136 ;
137 [label=<gini = 0.0<br/>samples = 2<br/>value = [2, 0]<br/>class = 0>, fillcolor="#e58139"] ;
136 -> 137 ;
138 [label=<pregnant &le; 4.5<br/>gini = 0.375<br/>samples = 4<br/>value = [1, 3]<br/>class = 1>, fillcolor="#7bbeee"] ;
136 -> 138 ;
139 [label=<gini = 0.0<br/>samples = 3<br/>value = [0, 3]<br/>class = 1>, fillcolor="#399de5"] ;
138 -> 139 ;
140 [label=<gini = 0.0<br/>samples = 1<br/>value = [1, 0]<br/>class = 0>, fillcolor="#e58139"] ;
138 -> 140 ;
141 [label=<gini = 0.0<br/>samples = 5<br/>value = [5, 0]<br/>class = 0>, fillcolor="#e58139"] ;
135 -> 141 ;
142 [label=<pedigree &le; 0.535<br/>gini = 0.346<br/>samples = 9<br/>value = [2, 7]<br/>class = 1>, fillcolor="#72b9ec"] ;
134 -> 142 ;
143 [label=<gini = 0.0<br/>samples = 6<br/>value = [0, 6]<br/>class = 1>, fillcolor="#399de5"] ;
142 -> 143 ;
144 [label=<bmi &le; 35.45<br/>gini = 0.444<br/>samples = 3<br/>value = [2, 1]<br/>class = 0>, fillcolor="#f2c09c"] ;
142 -> 144 ;
145 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
144 -> 145 ;
146 [label=<gini = 0.0<br/>samples = 2<br/>value = [2, 0]<br/>class = 0>, fillcolor="#e58139"] ;
144 -> 146 ;
147 [label=<glucose &le; 157.5<br/>gini = 0.219<br/>samples = 16<br/>value = [14, 2]<br/>class = 0>, fillcolor="#e99355"] ;
133 -> 147 ;
148 [label=<bmi &le; 43.4<br/>gini = 0.124<br/>samples = 15<br/>value = [14, 1]<br/>class = 0>, fillcolor="#e78a47"] ;
147 -> 148 ;
149 [label=<gini = 0.0<br/>samples = 13<br/>value = [13, 0]<br/>class = 0>, fillcolor="#e58139"] ;
148 -> 149 ;
150 [label=<insulin &le; 70.0<br/>gini = 0.5<br/>samples = 2<br/>value = [1, 1]<br/>class = 0>, fillcolor="#ffffff"] ;
148 -> 150 ;
151 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
150 -> 151 ;
152 [label=<gini = 0.0<br/>samples = 1<br/>value = [1, 0]<br/>class = 0>, fillcolor="#e58139"] ;
150 -> 152 ;
153 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
147 -> 153 ;
154 [label=<gini = 0.0<br/>samples = 2<br/>value = [0, 2]<br/>class = 1>, fillcolor="#399de5"] ;
132 -> 154 ;
155 [label=<bmi &le; 34.05<br/>gini = 0.405<br/>samples = 46<br/>value = [13, 33]<br/>class = 1>, fillcolor="#87c4ef"] ;
129 -> 155 ;
156 [label=<bp &le; 75.0<br/>gini = 0.49<br/>samples = 21<br/>value = [9, 12]<br/>class = 1>, fillcolor="#cee6f8"] ;
155 -> 156 ;
157 [label=<gini = 0.0<br/>samples = 4<br/>value = [4, 0]<br/>class = 0>, fillcolor="#e58139"] ;
156 -> 157 ;
158 [label=<pedigree &le; 0.436<br/>gini = 0.415<br/>samples = 17<br/>value = [5, 12]<br/>class = 1>, fillcolor="#8bc6f0"] ;
156 -> 158 ;
159 [label=<pedigree &le; 0.371<br/>gini = 0.496<br/>samples = 11<br/>value = [5, 6]<br/>class = 1>, fillcolor="#deeffb"] ;
158 -> 159 ;
160 [label=<bmi &le; 29.7<br/>gini = 0.444<br/>samples = 9<br/>value = [3, 6]<br/>class = 1>, fillcolor="#9ccef2"] ;
159 -> 160 ;
161 [label=<gini = 0.0<br/>samples = 3<br/>value = [0, 3]<br/>class = 1>, fillcolor="#399de5"] ;
160 -> 161 ;
162 [label=<bmi &le; 32.45<br/>gini = 0.5<br/>samples = 6<br/>value = [3, 3]<br/>class = 0>, fillcolor="#ffffff"] ;
160 -> 162 ;
163 [label=<pedigree &le; 0.164<br/>gini = 0.375<br/>samples = 4<br/>value = [3, 1]<br/>class = 0>, fillcolor="#eeab7b"] ;
162 -> 163 ;
164 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
163 -> 164 ;
165 [label=<gini = 0.0<br/>samples = 3<br/>value = [3, 0]<br/>class = 0>, fillcolor="#e58139"] ;
163 -> 165 ;
166 [label=<gini = 0.0<br/>samples = 2<br/>value = [0, 2]<br/>class = 1>, fillcolor="#399de5"] ;
162 -> 166 ;
167 [label=<gini = 0.0<br/>samples = 2<br/>value = [2, 0]<br/>class = 0>, fillcolor="#e58139"] ;
159 -> 167 ;
168 [label=<gini = 0.0<br/>samples = 6<br/>value = [0, 6]<br/>class = 1>, fillcolor="#399de5"] ;
158 -> 168 ;
169 [label=<pedigree &le; 1.088<br/>gini = 0.269<br/>samples = 25<br/>value = [4, 21]<br/>class = 1>, fillcolor="#5fb0ea"] ;
155 -> 169 ;
170 [label=<insulin &le; 306.5<br/>gini = 0.172<br/>samples = 21<br/>value = [2, 19]<br/>class = 1>, fillcolor="#4ea7e8"] ;
169 -> 170 ;
171 [label=<pedigree &le; 0.222<br/>gini = 0.1<br/>samples = 19<br/>value = [1, 18]<br/>class = 1>, fillcolor="#44a2e6"] ;
170 -> 171 ;
172 [label=<pregnant &le; 6.5<br/>gini = 0.444<br/>samples = 3<br/>value = [1, 2]<br/>class = 1>, fillcolor="#9ccef2"] ;
171 -> 172 ;
173 [label=<gini = 0.0<br/>samples = 1<br/>value = [1, 0]<br/>class = 0>, fillcolor="#e58139"] ;
172 -> 173 ;
174 [label=<gini = 0.0<br/>samples = 2<br/>value = [0, 2]<br/>class = 1>, fillcolor="#399de5"] ;
172 -> 174 ;
175 [label=<gini = 0.0<br/>samples = 16<br/>value = [0, 16]<br/>class = 1>, fillcolor="#399de5"] ;
171 -> 175 ;
176 [label=<insulin &le; 356.0<br/>gini = 0.5<br/>samples = 2<br/>value = [1, 1]<br/>class = 0>, fillcolor="#ffffff"] ;
170 -> 176 ;
177 [label=<gini = 0.0<br/>samples = 1<br/>value = [1, 0]<br/>class = 0>, fillcolor="#e58139"] ;
176 -> 177 ;
178 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
176 -> 178 ;
179 [label=<insulin &le; 147.5<br/>gini = 0.5<br/>samples = 4<br/>value = [2, 2]<br/>class = 0>, fillcolor="#ffffff"] ;
169 -> 179 ;
180 [label=<gini = 0.0<br/>samples = 2<br/>value = [2, 0]<br/>class = 0>, fillcolor="#e58139"] ;
179 -> 180 ;
181 [label=<gini = 0.0<br/>samples = 2<br/>value = [0, 2]<br/>class = 1>, fillcolor="#399de5"] ;
179 -> 181 ;
182 [label=<pedigree &le; 1.157<br/>gini = 0.219<br/>samples = 56<br/>value = [7, 49]<br/>class = 1>, fillcolor="#55abe9"] ;
128 -> 182 ;
183 [label=<pedigree &le; 0.343<br/>gini = 0.147<br/>samples = 50<br/>value = [4, 46]<br/>class = 1>, fillcolor="#4aa6e7"] ;
182 -> 183 ;
184 [label=<age &le; 48.5<br/>gini = 0.332<br/>samples = 19<br/>value = [4, 15]<br/>class = 1>, fillcolor="#6eb7ec"] ;
183 -> 184 ;
185 [label=<glucose &le; 177.0<br/>gini = 0.219<br/>samples = 16<br/>value = [2, 14]<br/>class = 1>, fillcolor="#55abe9"] ;
184 -> 185 ;
186 [label=<gini = 0.0<br/>samples = 9<br/>value = [0, 9]<br/>class = 1>, fillcolor="#399de5"] ;
185 -> 186 ;
187 [label=<pedigree &le; 0.206<br/>gini = 0.408<br/>samples = 7<br/>value = [2, 5]<br/>class = 1>, fillcolor="#88c4ef"] ;
185 -> 187 ;
188 [label=<gini = 0.0<br/>samples = 1<br/>value = [1, 0]<br/>class = 0>, fillcolor="#e58139"] ;
187 -> 188 ;
189 [label=<glucose &le; 187.5<br/>gini = 0.278<br/>samples = 6<br/>value = [1, 5]<br/>class = 1>, fillcolor="#61b1ea"] ;
187 -> 189 ;
190 [label=<gini = 0.0<br/>samples = 4<br/>value = [0, 4]<br/>class = 1>, fillcolor="#399de5"] ;
189 -> 190 ;
191 [label=<insulin &le; 65.0<br/>gini = 0.5<br/>samples = 2<br/>value = [1, 1]<br/>class = 0>, fillcolor="#ffffff"] ;
189 -> 191 ;
192 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
191 -> 192 ;
193 [label=<gini = 0.0<br/>samples = 1<br/>value = [1, 0]<br/>class = 0>, fillcolor="#e58139"] ;
191 -> 193 ;
194 [label=<glucose &le; 184.5<br/>gini = 0.444<br/>samples = 3<br/>value = [2, 1]<br/>class = 0>, fillcolor="#f2c09c"] ;
184 -> 194 ;
195 [label=<gini = 0.0<br/>samples = 2<br/>value = [2, 0]<br/>class = 0>, fillcolor="#e58139"] ;
194 -> 195 ;
196 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
194 -> 196 ;
197 [label=<gini = 0.0<br/>samples = 31<br/>value = [0, 31]<br/>class = 1>, fillcolor="#399de5"] ;
183 -> 197 ;
198 [label=<age &le; 28.0<br/>gini = 0.5<br/>samples = 6<br/>value = [3, 3]<br/>class = 0>, fillcolor="#ffffff"] ;
182 -> 198 ;
199 [label=<gini = 0.0<br/>samples = 2<br/>value = [0, 2]<br/>class = 1>, fillcolor="#399de5"] ;
198 -> 199 ;
200 [label=<glucose &le; 168.0<br/>gini = 0.375<br/>samples = 4<br/>value = [3, 1]<br/>class = 0>, fillcolor="#eeab7b"] ;
198 -> 200 ;
201 [label=<gini = 0.0<br/>samples = 1<br/>value = [0, 1]<br/>class = 1>, fillcolor="#399de5"] ;
200 -> 201 ;
202 [label=<gini = 0.0<br/>samples = 3<br/>value = [3, 0]<br/>class = 0>, fillcolor="#e58139"] ;
200 -> 202 ;
}

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetes.png')
Image(graph.create_png())


clf = DecisionTreeClassifier(max_depth=3)

clf = clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

dot_data = StringIO() #Where we will store the data from our decision tree classifier as text.

export_graphviz(clf, out_file=dot_data, filled=True, rounded=True, special_characters=True, feature_names=features, class_names=['0','1'])

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetes.png')
Image(graph.create_png())



































