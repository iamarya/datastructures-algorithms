<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Inheritance&nbsp;</strong></h2><p>&nbsp;</p><p>● Inheritance is a powerful feature in Object-Oriented Programming.</p><p>&nbsp;</p><p>● Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another. With the use of inheritance, the information is made manageable in a hierarchical order.</p><p>&nbsp;</p><p>● The class which inherits the properties of the other is known as <strong>subclass</strong> (derived class or child class) and the class whose properties are inherited is known as <strong>superclass</strong> (base class, parent class).</p><p>&nbsp;</p><p>Let us take a real-life example to understand inheritance. Let’s assume that Human is a class that has properties such as height, weight, age, etc and functionalities (or methods) such as eating(), sleeping(), dreaming(), working(), etc. Now we want to create Male and Female classes. Both males and females are humans and they share some common properties (like height, weight, age, etc) and behaviours (or functionalities like eating(), sleeping(), etc), so they can inherit these properties and functionalities from the Human class. Both males and females have some characteristics specific to them (like men have short hair and females have long hair). Such properties can be added to the Male and Female classes separately. This approach makes us write less code as both the classes inherit several properties and functions from the superclass, thus we didn’t have to re-write them. Also, this makes it easier to read the code.</p><p>&nbsp;</p><h2><strong>Python Inheritance Syntax</strong></h2><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SuperClass</span>:</span>
 &nbsp;<span class="hljs-comment">#Body of base class </span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SubClass</span>(<span class="hljs-params">BaseClass</span>):</span>
 &nbsp;<span class="hljs-comment">#Body of derived class</span></code></pre><p><br>The name of the superclass is passed as a parameter in the subclass while declaration.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><p>To demonstrate the use of inheritance, let us take an example.</p><p>A polygon is a closed figure with 3 or more sides. Say, we have a class called Polygon defined as follows.</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Polygon</span>:</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self, no_of_sides</span>):</span> <span class="hljs-comment">#Constructor</span>
 &nbsp;&nbsp;&nbsp;self.n = no_of_sides
 &nbsp;&nbsp;&nbsp;self.sides = [<span class="hljs-number">0</span> <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(no_of_sides)]
 &nbsp;&nbsp; 
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">inputSides</span>(<span class="hljs-params">self</span>):</span> <span class="hljs-comment">#Take user input for side lengths</span>
 &nbsp;&nbsp;&nbsp;self.sides=[int(input(<span class="hljs-string">"Enter side: "</span>))<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(self.n)]


<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">displaySides</span>(<span class="hljs-params">self</span>):</span> <span class="hljs-comment">#Print the sides of the polygon</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(self.n):
 &nbsp;&nbsp;&nbsp;print(<span class="hljs-string">"Side"</span>,i+<span class="hljs-number">1</span>,<span class="hljs-string">"is"</span>,self.sides[i])</code></pre><p>&nbsp;</p><p>This class has <strong>data attributes</strong> to store the number of sides n and magnitude of each side as a list called <strong>sides</strong>.</p><p>The <strong>inputSides()</strong> method takes in the magnitude of each side and <strong>dispSides()</strong> displays these side lengths.</p><p><br>Now, a triangle is a <strong>polygon</strong> with 3 sides. So, we can create a class called <strong>Triangle</strong> which inherits from <strong>Polygon</strong>. In other words, we can say that every <strong>triangle</strong> is a <strong>polygon</strong>. This makes all the attributes of the <strong>Polygon</strong> class available to the <strong>Triangle</strong> class.</p><p>&nbsp;</p><h2><strong>Constructor in Subclass</strong></h2><p>&nbsp;</p><p>The constructor of the subclass must call the constructor of the superclass by accessing the <strong>__init__ </strong>method of the superclass in the following format:</p><p>&nbsp;</p><pre><code class="language-python hljs">&lt;SuperClassName&gt;.__init__(self,&lt;Parameter1&gt;,&lt;Parameter2&gt;,...)</code></pre><p>&nbsp;</p><p><strong>Note:</strong> The parameters being passed in this call must be the same as the parameters being passed in the superclass’ <strong>__init__ </strong>function, otherwise it will throw an error.</p><p><br><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">subclass</span>(<span class="hljs-params">superclass</span>):</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;superclass.__init__(self,arg,...)
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="hljs-comment">#Calling constructor of the superclass</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><p>The <strong>Triangle</strong> class can be defined as follows.</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Polygon</span>:</span>
    
    <span class="hljs-comment">#Constructor</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self, no_of_sides</span>):</span>
        self.n = no_of_sides
        self.sides = [<span class="hljs-number">0</span> <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(no_of_sides)]
        
    <span class="hljs-comment">#Take user input for side lenghts    </span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">inputSides</span>(<span class="hljs-params">self</span>):</span>
        self.sides = [int(input(<span class="hljs-string">"Enter Side: "</span>)) <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(self.n)]
        
    <span class="hljs-comment">#Print the sides of the polygon</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">displaySides</span>(<span class="hljs-params">self</span>):</span>
        <span class="hljs-keyword">for</span> i <span class="hljs-keyword">in</span> range(self.n):
            print(<span class="hljs-string">"Side"</span>,i+<span class="hljs-number">1</span>,<span class="hljs-string">"is"</span>,self.sides[i])
            
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Triangle</span>(<span class="hljs-params">Polygon</span>):</span>
    
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self</span>):</span>
        <span class="hljs-comment">#Calling constructor of superclass</span>
        Polygon.__init__(self, <span class="hljs-number">3</span>)
        
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">findArea</span>(<span class="hljs-params">self</span>):</span>
        a, b, c = self.sides
        <span class="hljs-comment">#Calculate the semi-perimeter</span>
        s = (a + b + c) / <span class="hljs-number">2</span>
        area = (s * (s-a) * (s-b) * (s-c)) ** <span class="hljs-number">0.5</span>
        print(<span class="hljs-string">'The area of the triangle is %0.2f'</span> %area)</code></pre><p><br>However, the class <strong>Triangle</strong> has a new method<strong> findArea()</strong> to find and print the area of the triangle. This method is only specific to the Triangle class and not the <strong>Polygon</strong> class. Here is a sample run:</p><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-meta">&gt;&gt;&gt; </span>t = Triangle() <span class="hljs-comment">#Instantiating a Triangle object </span>
<span class="hljs-meta">&gt;&gt;&gt; </span>t.inputSides()
Enter side <span class="hljs-number">1</span>: <span class="hljs-number">3</span>
Enter side <span class="hljs-number">2</span>: <span class="hljs-number">5</span> 
Enter side <span class="hljs-number">3</span>: <span class="hljs-number">4</span> 


<span class="hljs-meta">&gt;&gt;&gt; </span>t.dispSides() 
Side <span class="hljs-number">1</span> <span class="hljs-keyword">is</span> <span class="hljs-number">3</span> 
Side <span class="hljs-number">2</span> <span class="hljs-keyword">is</span> <span class="hljs-number">5</span> 
Side <span class="hljs-number">3</span> <span class="hljs-keyword">is</span> <span class="hljs-number">4</span> 


<span class="hljs-meta">&gt;&gt;&gt; </span>t.findArea() 
The area of the triangle <span class="hljs-keyword">is</span> <span class="hljs-number">6.00</span></code></pre><p>&nbsp;</p><p>We can see that even though we did not define methods like <strong>inputSides()</strong> or <strong>displaySides()</strong> for class Triangle separately, we were able to use them. If an attribute is not found in the subclass itself, the search continues to the superclass.</p><p>&nbsp;</p><p>Please note that there are several types of inheritance in Python which are discussed in the upcoming topics. The one that we discussed in this section is the basic inheritance type and is called <i><strong>Single Inheritance.</strong></i></p><p>&nbsp;</p></div></div>