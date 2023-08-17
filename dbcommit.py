import sqlite3

conn = sqlite3.connect("Maths_Topics.db")

cur = conn.cursor()


statement = "CREATE TABLE Questions (id UNIQUE AUTOINCREMENT, topic_id int, image largeblob, answer varchar(1000))"

data=()

cur.execute(statement, data)



conn.commit();

cur.close()
conn.close()




conn.execute(""" CREATE TABLE IF NOT EXISTS Topics(topic_name TEXT, topic_score INTEGER,  topic_max_score INTEGER)""")
#statement = "INSERT INTO Topics (topic_name, topic_score) VALUES (?, ?)";
'''
DATALISTX = [
("Direct Proof, by Exhaustion, Counter Example, Joting", 0,
,("Proof by Contradiction", 0)
,("Polynomials", 0)
,("Factor Theorem", 0)
,("Algebraic Division", 0)
,("Algebraic Fractions", 0)
,("Partial Fractions", 0)
,("Quadratic Graphs", 0)
,("Modelling with Quadratic", 0)
,("Discriminant", 0)
,("Simultaneous Equations", 0)
,("Inequalities", 0)
,("Cubic Graphs", 0)
,("Modulus Function Graph", 0)
,("Equation Involving Modulus", 0)
,("Function Graphs", 0)
,("Graph Transformations", 0)
,("Composite and Inverse Functions", 0)
,("Straight Lines", 0)
,("Circle Geometry", 0)
,("Parametric Equations", 0)
,("Arithmetic Series", 0)
,("Geometric Series", 0)
,("Sigma Notation", 0)
,("Binomial Expansion", 0)
,("Trigonometry Basics", 0)
,("Arc length & Area of a Sector", 0)
,("Sine & Cosine Rules", 0)
,("Trig Graphs", 0)
,("Trig Equations", 0)
,("Basic Trig Identities", 0)
,("Inverse Trig Functions", 0)
,("Reciprocal Trig Functions", 0)
,("Addition and Double Angle", 0)
,("Formulae", 0)
,("Other Identities", 0)
,("Rcos(x+a) or Rsin(x+a)", 0)
,("Trig Proofs", 0)
,("Small Angle Approximation", 0)
,("Laws of Logarithms", 0)
,("Equations Involving Exponentials", 0)
,("Equations Involving Logarithms", 0)
,("Reduction to Linear Form", 0)
,("Rate of Change - wordy", 0)
,("Basic Differentiation", 0)
,("Gradients, Tangents and Normals", 0)
,("Differentiation from First", 0)
,("Principles", 0)
,("Stationary Points", 0)
,("Convex, Concave, Pt of Inflection", 0)
,("Chain Rule", 0)
,("Differentiating Exp Functions", 0)
,("Differentiating Trig Functions", 0)
,("Product Rule", 0)
,("Quotient Rule", 0)
,("Differentiating Parametric", 0)
,("Equations", 0)
,("Implicit Differentiation", 0)
,("Integration to Find f(x)", 0)
,("Lim Sigma 𝛿𝛿𝛿𝛿 as Integral", 0)
,("Properties of Integral", 0)
,("Definite Integrals / Area", 0)
,("Parametric Integrals", 0)
,("Integrating Exponentials", 0)
,("Integrating Trig Functions", 0)
,("Reverse Chain Rule", 0)
,("Integration by Substitution", 0)
,("Integration by Parts", 0)
,("Solving Differential Equations", 0)
,("Locating Roots", 0)
,("Iteration", 0)
,("Newton-Raphson Method", 0)
,("Trapezium Rule", 0)
,("Vector Basics", 0)
,("Vector Calculations", 0)
,("Proof with Vectors", 0)
,("3D Vector", 0)
]

for i in range (0, len(DATALISTX)):
    statement = "INSERT INTO Topics (topic_name, topic_score, topic_max_score) VALUES (?, ?, ?);"
    data = (DATALISTX[i][0], 0, 0)
    cur.execute(statement, data)
    conn.commit(); 



cur.execute(statement, data)

conn.commit();

cur.close()
conn.close()

