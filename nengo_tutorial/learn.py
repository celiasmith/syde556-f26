import nengo
import numpy as np
from nengo.processes import WhiteSignal

model = nengo.Network(label="Learning") #seed=7
with model:
    pre = nengo.Ensemble(50, dimensions=1, label="Pre")
    #post = nengo.Ensemble(50, dimensions=1, label="Post")
    post = nengo.Node(size_in=1, label="Output")

    error = nengo.Node(size_in=1, label="Error")


    # Error = pre - post
    # Learn the square function
    # nengo.Connection(pre, error, function=lambda x: x**2, transform=-1)
    nengo.Connection(pre, error, transform=-1)
    nengo.Connection(post, error, transform=1)

    # Connecting pre population 
    conn = nengo.Connection(
        pre,
        post,
        function=lambda x: np.random.random(1),
        solver=nengo.solvers.LstsqL2(weights=True),
        learning_rule_type=nengo.PES(learning_rate=1e-4)
    )

    nengo.Connection(error, conn.learning_rule)

    # Providing input to the model
    stim = nengo.Node(WhiteSignal(30, high=10))  # RMS = 0.5 by default
    nengo.Connection(stim, pre) 
