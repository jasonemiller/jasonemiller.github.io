<!-- originally from http://www.sfu.ca/~jtmulhol/calculus-applets/html/sagemath-cell-approximate-integration.html -->

<head>
		<meta charset="utf-8">
		<meta name="generator" content="pandoc">
		<title>Approximate Integration in SageMath</title>
		<link rel="shortcut icon" type="image/x-icon" href="/favicon.ico" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<link rel="stylesheet" type="text/css" href="../css/bootstrap/bootstrap.css" />
		<link rel="stylesheet" type="text/css" href="../css/bootstrap/bootstrap-theme.css" />
		<link rel="stylesheet" type="text/css" href="../css/swc.css" />

		<!-- begin: Sage Single Cell preamble -->
		<script src="https://sagecell.sagemath.org/static/jquery.min.js"></script>
    <script src="https://sagecell.sagemath.org/embedded_sagecell.js"></script><script>$(function () {
    // Make the div with id 'mycell' a Sage cell
    sagecell.makeSagecell({inputLocation:  '#mycell',
                           template:       sagecell.templates.minimal,
                           evalButtonText: 'Activate'});
    // Make *any* div with class 'compute' a Sage cell
    sagecell.makeSagecell({inputLocation: 'div.compute',
                           evalButtonText: 'Evaluate'});
	  sagecell.makeSagecell({inputLocation: '#sagecell1',
													 replaceOutput: true,
													 hide: ['messages', 'computationID', 'files', 'sageMode',
							 					 					'editorToggle', 'sessionTitle', 'done'],
													 evalButtonText: 'Evaluate'});
		sagecell.makeSagecell({inputLocation: '#sagecell2',
													 replaceOutput: true,
													 hide: ['messages', 'computationID', 'files', 'sageMode',
							 					 					'editorToggle', 'sessionTitle', 'done'],
													 evalButtonText: 'Evaluate'})            ;
		sagecell.makeSagecell({inputLocation: '#sagecell3',
													 replaceOutput: true,
													 hide: ['messages', 'computationID', 'files', 'sageMode',
							 					 					'editorToggle', 'sessionTitle', 'done'],
													evalButtonText: 'Evaluate'});
		sagecell.makeSagecell({inputLocation: '#sagecell4',
													 replaceOutput: true,
													 hide: ['messages', 'computationID', 'files', 'sageMode',
							 					 					'editorToggle', 'sessionTitle', 'done'],
													 evalButtonText: 'Evaluate'});
		sagecell.makeSagecell({inputLocation: '#sagecell5',
													 replaceOutput: true,
													 hide: ['messages', 'computationID', 'files', 'sageMode',
							 					 					'editorToggle', 'sessionTitle', 'done'],
													 evalButtonText: 'Evaluate'});
    });
		</script>
		<!-- end: Sage Single Cell preamble -->


		<!--  begin MathJax preamble -->
<!--		<script type="text/javascript"src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script> -->
		<!-- end MathJax preamble -->

</head>


<body class="lesson">

	<div class="container card">
		<article>
		<div class="row">
			<div class="col-md-10 col-md-offset-1">
				<h1 class="title">Approximate Integration:</h1>

				<p>Implementations of the following numerical integration techniques are given below:
				<a href="#lh">Left-hand Riemann sum</a>,
				<a href="#rh">Right-hand Riemann sum</a>,
				<a href="#mr">Midpoint Rule</a>,
				<a href="#tr">Trapezoid Rule</a>, and
				<a href="#sr">Simpson's Rule</a>.
				Modify and evaluate the SageMath code as you wish.   </p>

				<p>Each function takes as input a
				function \(f\), an interval \([a,b]\), and an integer \(n\). Recall \(\Delta x = \frac{b-a}{n}\) and \(x_i = a+i\Delta x\) for each \(0\le i \le n\).</p>

				<h2>Syntax for entering mathematical expressions in SageMath</h2>
				<p><ul>
					<li><p> Use <code>*</code> for multiplication, for example 10x would be input as <code>10*x</code>. </p></li>
					<li><p> Powers of x are input using <code>^</code>.  For example the square function \(x^2\) is input as <code>x^2</code>.</p></li>
					<li><p> The exponential function \(e^x\) is input as <code>exp(x)</code>. </p></li>
					<li><p> The natural logarithm \(\ln(x)\) (i.e. base e) is input as <code>log(x)</code> or <code>ln(x)</code>.</p></li>
				</ul>
				</p>




				<h3><a name="lh">Left-Hand Riemann Sum:</a></h3>
				<p>
				The function <code>lefthand_rs</code> outputs the
				left-hand Riemann sum approximation of \(\int_a^b f(x) dx\)
				using n partitions of the interval:
				$$\int_a^bf(x)dx \approx \sum_{i=1}^n f(x_{i-1})\Delta x = \Delta x(f(x_0)+f(x_1)+\cdots +f(x_{n-1})).$$
				</p>
				<div class="compute" id="sagecell1"><script type="text/code">def lefthand_rs(fcn,a,b,n):
	# output: left-hand riemann sum approx of int_a^n fcn(x)dx using n steps
	Deltax = (b-a)*1.0/n
	return Deltax*sum([fcn(a+Deltax*i) for i in range(n)])

#Example
n=6
a=0
b=1
f(x)=sin(x)
lefthand_rs(f,a,b,n).n();
				</script></div>


				<h3><a name="rh">Right-Hand Riemann Sum:</a></h3>
				<p>
				The function <code>righthand_rs</code> outputs the
				right-hand Riemann sum approximation of \(\int_a^b f(x) dx\)
				using n partitions of the interval:
				$$\int_a^bf(x)dx \approx \sum_{i=1}^n f(x_{i})\Delta x = \Delta x(f(x_1)+f(x_1)+\cdots +f(x_{n})).$$
				</p>
				<div class="compute" id="sagecell2"><script type="text/code">def righthand_rs(fcn,a,b,n):
# output: right-hand riemann sum approx of int_a^b fcn(x)dx using n steps
	Deltax = (b-a)*1.0/n
	return Deltax*sum([fcn(a+Deltax*(i+1)) for i in range(n)])

#Example
n=20
a=0
b=1
f(x)=sin(x)
righthand_rs(f,a,b,n).n();
				</script></div>


				<h3><a name="mr">Midpoint Rule:</a></h3>
				<p>
				The function <code>midpoint_rule</code> outputs the
				midpoint rule approximation of \(\int_a^b f(x) dx\) using n partitions of the interval:
				$$\int_a^bf(x)dx \approx \sum_{i=1}^n f(\overline{x}_{i-1})\Delta x,$$
				where \(\overline{x}_i\) is the midpoint of inteval \([x_{i-1},x_i]\), which is \(\overline{x}_i=\frac{x_{i-1}+x_i}{2}\).
				</p>
				<div class="compute" id="sagecell3"><script type="text/code">def midpoint_rule(fcn,a,b,n):
# output: midpoint rule approx of int_a^b fcn(x)dx using n steps
	Deltax = (b-a)*1.0/n
	xs=[a+Deltax*i for i in range(n+1)]
	ysmid=[fcn((xs[i]+xs[i+1])/2) for i in range(n)]
	return Deltax*sum(ysmid)

#Example
n=10;
a=0
b=1
f(x)=sin(x)
print midpoint_rule(f,a,b,n).n();
				</script></div>


				<h3><a name="tr">Trapezoid Rule:</a></h3>
				<p>
				The function <code>trapezoid_rule</code> outputs the
				trapezoid rule approximation of \(\int_a^b f(x) dx\) using n partitions of the interval:
				$$\int_a^bf(x)dx \approx \frac{\Delta x}{2}(f(x_0)+2f(x_1)+2f(x_2)+ \cdots + 2f(x_{n-1})+f(x_n)).$$
				</p>
				<div id="sagecell4"><script type="text/code">def trapezoid_rule(fcn,a,b,n):
# output: trapezoid rule approx of int_a^b fcn(x)dx using n steps
	Deltax = (b-a)*1.0/n
	coeffs = [2]*(n-1)
	coeffs = [1]+coeffs+[1]
	valsf = [fcn(a+Deltax*i) for i in range(n+1)]
	return (Deltax/2)*sum([coeffs[i]*valsf[i] for i in range(n+1)])

#Example
n=10;
a=0
b=1
f(x)=sin(x)
trapezoid_rule(f,a,b,n).n();
				</script></div>


				<h3><a name="sr">Simpsons Rule:</a></h3>
				<p>
				The function <code>simpsons_rule</code> outputs the
				Simpson's Rule approximation of \(\int_a^b f(x) dx\) using n partitions
				of the interval:
				$$\int_a^bf(x)dx \approx \frac{\Delta x}{3}(f(x_0)+4f(x_1)+2f(x_2)+4f(x_3)+ \cdots + 2f(x_{n-2})+4f(x_{n-1})+f(x_n)).$$
				<b>Note:</b> n must be even.
				</p>
				<div id="sagecell5"><script type="text/code">def simpsons_rule(fcn,a,b,n):
# output: simpsons rule approx of int_a^b fcn(x)dx using n steps (n must be an even integer)
	Deltax = (b-a)*1.0/n
	n2=int(n/2)
	coeffs = [4,2]*n2
	coeffs = [1] +coeffs[:n-1]+[1]
	valsf = [fcn(a+Deltax*i) for i in range(n+1)]
	return (Deltax/3)*sum([coeffs[i]*valsf[i] for i in range(n+1)])

#Example
n=6;
a=0
b=1
f(x)=sin(x)
simpsons_rule(f,a,b,n).n();
				</script></div>

<br /><br />



<h4> Piecewise Defined Functions:</h4>

Sometimes you may find the need to define \(f\) as a piecewise defined function.  For example, suppose you are trying to approximate the integral \(\int_{0}^{10} f(x)~dx\) where
$$f(x)=\begin{cases}
\displaystyle x,&x\le 5\\
x^2,&x > 5\\
\end{cases}
$$ (not that you would not need to approximate in this case since you can easily find antiderivates, but we'll just use it as a simple example).

</br></br>

We can replace the line "f(x) = ..." in the code above with a python function defining \(f\):

<pre class="gap"><code>def f(x):
    if x<=5:
        return x;
    elif x>5:   # elif means "else if"
        return x^2;</code></pre>

Try to cut-and-paste this code to replace the function \(f\) in Simpson's Rule above.

<h4>Bonus calculation SageMath cell</h4>

Use this cell for other calculating needs.

<div class="compute" id="sagecell6"><script type="text/code">
#Example
x=55;
y=pi;
(x-y).n();
</script></div>


<hr>

<p>The original version of this page by Dr. Jamie Mulholland (Simon Frasier University) can be found at <a href="http://www.sfu.ca/~jtmulhol/calculus-applets/html/sagemath-cell-approximate-integration.html">http://www.sfu.ca/~jtmulhol/calculus-applets/html/sagemath-cell-approximate-integration.html</a>.
<br /><br />


</div>
<!-- Javascript placed at the end of the document so the pages load faster -->
<!--<script src="http://software-carpentry.org/v5/js/jquery-1.9.1.min.js"></script>-->
<script src="css/bootstrap/bootstrap-js/bootstrap.js"></script>