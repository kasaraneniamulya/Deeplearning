
#Importing tensorflow library
import tensorflow as tf

#Taking a 2*2 matrix
a=tf.constant([1,2,3,4], shape=(2,2))

#making square of A matrix
x=tf.pow(a,2)

#Taking another 2*2 matrix
b=tf.constant([4,4,4,4], shape=(2,2))

#Adding that squared matrix A^2 with the above matrix B
y=tf.add(x,b)

#taking another matrix C
c=tf.constant([2,2,2,2], shape=(2,2))

#Multiplying the whole (A^2+B) with C
z=tf.matmul(y,c)

with tf.Session() as sess:
    print("A square: ")
    print(sess.run(x))
    print("A square plus B: ")
    print(sess.run(y))
    print("(A square plus B)plus C: ")
    print(sess.run(z))
