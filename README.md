#AlgorithmOcean Back End

<!DOCTYPE html>
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark">

<body>
	<p>To see the backend in action, you can <a href="https://algorithmocean.herokuapp.com/createaccount">create an account</a></p>
	<h2>Project Description</h2>
	<p>AlgorithmOcean is an app I created for an independent study course at Framingham State University from April - July 2022</p>
	<h2>Purpose</h2>
	<ul>
		<li>It's the first free, online, interactive algorithm-learning resource</li>
		<li>Introduces high schoolers and young adults to algorithms without needing coding experience</li>
		<li>Connects algorithms with science facts to make learning fun and relevant</li>
	</ul>
	<h2>React Back End</h2>
	<ul>
		<li>PostgreSQL database stores user account information and practice scores</li>
		<li>Django processes GET, POST, and PUT requests from the front end</li>
		<li>Custom Django authentication used to login users via POST request from front-end</li>
	</ul>
	<h2>React Front End</h2>
	<ul>
		<li>Interactive lesson page has users perform algorithms on screen</li>
		<li>Program randomly generates an array of numbers and performs the specified sort behind the scenes</li>
		<li>User moves are compared to program moves to score the user's answer</li>
		<li>Educational videos, directions about how to use the program, and other features available</li>
		<li>Followed ARIA specifications for color contrast, keyboard navigation, and screen reader accessibility</li>
	</ul>
	<p>For details, please see <a href="https://github.com/KaySRubio/algorithmOcean">front end</a></p>
	<h2>Future directions</h2>
	<ul>
		<li>Expand the site to cover more complex algorithms</li>
		<li>Add teacher accounts so teachers can assign students lessons and view student scores</li>
		<li>Host front- and back-end on same domain to simplify CORS/CSRF issues</li>
	</ul>
</body>
</html>
