<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Multilevel Inheritance</strong></h2><p>&nbsp;</p><p>We can also inherit from a derived class.</p><p>This is called <strong>multilevel inheritance</strong>. It can be of any depth in Python. An example is given below.</p><p><br><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SuperClass</span>:</span>
 <span class="hljs-keyword">pass</span> 

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SubClass</span>(<span class="hljs-params">SuperClass</span>):</span>
 <span class="hljs-keyword">pass</span>
 
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SubSubClass</span>(<span class="hljs-params">SubClass</span>):</span>
 <span class="hljs-keyword">pass</span></code></pre><p>&nbsp;</p><p>Here, <strong>SubClass</strong> is derived from <strong>SuperClass</strong>, and <strong>SubSubClass</strong> is derived from <strong>SubClass</strong>.<br>&nbsp;</p><figure class="image"><img src="https://lh6.googleusercontent.com/tVPFrZMGn5mzq_iWlN4crhBtHsnKOjQioNNaUaG5t4Pho0xI0Bd3GD9mm543ftCQxLew82Xl5TKB-8XRzH8p2Hu4sUk7pk98pf9Z9adrvZBhi8xnh5OBe3lTiXF-sMQm53In31y3"></figure><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span>:</span>
 &nbsp;&nbsp; 
 &nbsp;&nbsp;&nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self,name</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.name = name
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span>(<span class="hljs-params">A</span>):</span>
 &nbsp;&nbsp; 
 &nbsp;&nbsp;&nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self,name,age</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A.__init__(self,name)
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.age = age
 &nbsp;&nbsp; 
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span>(<span class="hljs-params">B</span>):</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self,name,age,rollno</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B.__init__(self,name,age)
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.rollno = rollno
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
s = C(<span class="hljs-string">"parikh"</span>,<span class="hljs-number">19</span>,<span class="hljs-number">1011</span>)
print(s.name)
print(s.age)
print(s.rollno)</code></pre><p><br><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">parikh
<span class="hljs-number">19</span>
<span class="hljs-number">1011</span></code></pre><p>&nbsp;</p><h2><strong>Method Resolution Order (MRO)</strong></h2><p>&nbsp;</p><p><strong>Method Resolution Order(MRO)</strong> denotes the way a programming language resolves a method or an attribute. It defines the order in which the subclasses are searched when a method is called. First, the method or the attribute is searched within the subclass and then it is searched in its parent class and so on.</p><p>&nbsp;</p><ul><li>Let's understand it through an example:</li></ul><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span>:</span>
 
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print</span>(<span class="hljs-params">self</span>):</span>
      print(<span class="hljs-string">"This is vehicle print"</span>)
     
     
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span>(<span class="hljs-params">Vehicle</span>):</span>
 
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print</span>(<span class="hljs-params">self</span>):</span>
      print(<span class="hljs-string">"This is Car print"</span>)
   
     
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Waganor</span>(<span class="hljs-params">Car</span>):</span>
   
   <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print</span>(<span class="hljs-params">self</span>):</span>
       print(<span class="hljs-string">"This is Waganor print"</span>)
       

<span class="hljs-comment">#Driver's code</span>

w = Waganor()
w.print()</code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">This <span class="hljs-keyword">is</span> Waganor <span class="hljs-keyword">print</span></code></pre><p>&nbsp;</p><p>In the above example, the method that is invoked is from the class <i><strong>Waganor</strong></i> but not from class <i><strong>Car</strong></i><strong> </strong>or<strong> </strong>class<strong> </strong><i><strong>Vehicle</strong></i>, and this is due to the Method Resolution Order(MRO). The order of priority that is followed in the above code is- <strong>class </strong><i><strong>Waganor</strong></i><strong> &nbsp;&gt; class </strong><i><strong>Car</strong></i><strong> &gt; class </strong><i><strong>Vehicle</strong></i>.</p><p>&nbsp;</p><p>if you want to get rid off of this ambiguity and want to call the print() method of any particular class we can use the syntax: <strong>ClassName.method(object)</strong>. Here binding the class <i><strong>Car</strong></i> and class <i><strong>vehicle</strong></i> with <i><strong>Waganor</strong></i> class object.&nbsp;</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span>:</span>
 
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print</span>(<span class="hljs-params">self</span>):</span>
      print(<span class="hljs-string">"This is vehicle print"</span>)
     
     
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span>(<span class="hljs-params">Vehicle</span>):</span>
 
  <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print</span>(<span class="hljs-params">self</span>):</span>
      print(<span class="hljs-string">"This is Car print"</span>)
   
     
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Waganor</span>(<span class="hljs-params">Car</span>):</span>
   
   <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print</span>(<span class="hljs-params">self</span>):</span>
       print(<span class="hljs-string">"This is Waganor print"</span>)
        

<span class="hljs-comment">#Driver's code</span>

w = Waganor()
Car.print(w)
Vehicle.print(w)</code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">This <span class="hljs-keyword">is</span> Car <span class="hljs-keyword">print</span>
This <span class="hljs-keyword">is</span> vehicle <span class="hljs-keyword">print</span></code></pre></div></div>