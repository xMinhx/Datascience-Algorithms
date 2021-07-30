# Linear program converter

This program converts given constraints and function into a linear program for GLPK

## Example 1 - Generate regression for given points (lp_regression.py)

```py
x = [1.55, 1.57, 1.62, 1.68, 1.75, 1.76, 1.81, 1.83, 1.87, 1.89, 1.9, 1.92, 1.95, 1.96, 1.99, 2.02]
y = [51, 50, 55, 52, 60, 68, 78, 91, 84, 81, 90, 105, 95, 99, 100, 101.0]
chosen function: y = x + c  -> ["c", "x"]  #lower exponents first

#create_lp_regression(variables, variable bounds, x-array, y-array, "minimize" | "maximize")
regression = create_lp_regression(["c", "x"], ["free", "free"], x, y, "minimize")
print(regression)
```

will generate:

```
minimize
	u0 + v0 + u1 + v1 + u2 + v2 + u3 + v3 + u4 + v4 + u5 + v5 + u6 + v6 + u7 + v7 + u8 + v8 + u9 + v9 + u10 + v10 + u11 + v11 + u12 + v12 + u13 + v13 + u14 + v14 + u15 + v15 

subject to
	 a + 1.55 b + u0 - v0 = 51.0
	 a + 1.57 b + u1 - v1 = 50.0
	 a + 1.62 b + u2 - v2 = 55.0
	 a + 1.68 b + u3 - v3 = 52.0
	 a + 1.75 b + u4 - v4 = 60.0
	 a + 1.76 b + u5 - v5 = 68.0
	 a + 1.81 b + u6 - v6 = 78.0
	 a + 1.83 b + u7 - v7 = 91.0
	 a + 1.87 b + u8 - v8 = 84.0
	 a + 1.89 b + u9 - v9 = 81.0
	 a + 1.9 b + u10 - v10 = 90.0
	 a + 1.92 b + u11 - v11 = 105.0
	 a + 1.95 b + u12 - v12 = 95.0
	 a + 1.96 b + u13 - v13 = 99.0
	 a + 1.99 b + u14 - v14 = 100.0
	 a + 2.02 b + u15 - v15 = 101.0

bounds
	a free
	b free
	
end
```

visualization of GLPK results:

![image](https://user-images.githubusercontent.com/55718218/127593267-a7fd6366-f2cc-40e0-9a3d-f91b1b1c2efb.png)


## Example 2 - Generate hyperplane for two given classes (lp_hyperplane.py)

```py 
hyper = create_lp_hyper(["c","x"], ["free", "free"], x1, y1, x2, y2, delta=False)
print(hyper)
```

will generate:

```
maximize
	delta

subject to
	 a + 0.6 b + delta <= 2.5
	 a + 1.0 b + delta <= 0.9
	 a + 1.5 b + delta <= 1.4
	 a + 2.5 b + delta <= 2.5
	 a + 2.9 b + delta <= 3.5
	 a + 3.0 b + delta <= 1.1
	 a + 4.4 b + delta <= 2.3
	 a + 5.6 b + delta <= 1.6
	 a + 6.0 b + delta <= 3.6
	 a + 7.5 b + delta <= 2.4
	 a + 8.6 b + delta <= 3.4
	 a + 10.6 b + delta <= 2.5

	 a + 1.4 b - delta >= -2.9
	 a + 2.6 b - delta >= -2.5
	 a + 2.7 b - delta >= -3.9
	 a + 3.5 b - delta >= -1.5
	 a + 3.6 b - delta >= -2.4
	 a + 4.1 b - delta >= -3.6
	 a + 5.2 b - delta >= -2.4
	 a + 5.5 b - delta >= -1.4
	 a + 5.8 b - delta >= -3.2
	 a + 7.2 b - delta >= -1.2
	 a + 7.6 b - delta >= -1.9
	 a + 9.6 b - delta >= 0.6
	 a + 9.9 b - delta >= -1.3
	 a + 11.1 b - delta >= 1.7

bounds
	a free
	b free
	delta >= 0
end
```

visualisation of GLPK results:

![image](https://user-images.githubusercontent.com/55718218/127593965-cd522033-9ff9-4ee9-a45f-c1cca6a53d02.png)
