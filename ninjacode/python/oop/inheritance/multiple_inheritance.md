<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Multiple Inheritance</strong></h2><p>&nbsp;</p><p>● A class can be inherited from more than one superclass in Python, similar to C++. This is called multiple inheritances.</p><p>&nbsp;● In multiple inheritance, the features of all the superclasses are inherited into the subclass. The syntax for multiple inheritance is similar to single inheritance.</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SuperClass1</span>:</span>
 <span class="hljs-keyword">pass</span>
 
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SuperClass2</span>:</span>
 <span class="hljs-keyword">pass</span>
 
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SubClass</span>(<span class="hljs-params">SuperClass1, SuperClass2</span>):</span>
 <span class="hljs-keyword">pass</span></code></pre><p>&nbsp;</p><p>Here, the SubClass class is derived from SuperClass1 and SuperClass2 classes and it has access to all the instance attributes and methods from both these superclasses.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span>:</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">test</span>(<span class="hljs-params">self</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(<span class="hljs-string">"print of A is called"</span>)
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span>:</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">test</span>(<span class="hljs-params">self</span>):</span>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(<span class="hljs-string">"print of B is called"</span>)
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span>(<span class="hljs-params">A,B</span>):</span>
 &nbsp;&nbsp;&nbsp;<span class="hljs-keyword">pass</span>

<span class="hljs-comment">#Driver's code</span>

o = C()
o.test()</code></pre><p><br>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-keyword">print</span> of A <span class="hljs-keyword">is</span> called</code></pre><p>&nbsp;</p><p>In <strong>multiple inheritances</strong>, the methods are executed based on the <strong>order specified while inheriting the classes</strong> (Order inside parenthesis). Let’s look over another example to deeply understand the method resolution order:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span>:</span>
 &nbsp;<span class="hljs-keyword">pass</span> 

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span>:</span>
 &nbsp;<span class="hljs-keyword">pass</span> 

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span>(<span class="hljs-params">A, B</span>):</span>
 &nbsp;<span class="hljs-keyword">pass</span></code></pre><p><br>The order in which the methods will be resolved will be C, A, B. This is because while inheriting the order is A, B.&nbsp;</p><p><strong>Methods for Method Resolution Order(MRO) of a class:</strong></p><p><br>To get the method resolution order of a class we can use the <strong>mro()</strong> method. By using this method we can display the order in which methods are resolved.</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span>:</span>
 &nbsp;<span class="hljs-keyword">pass</span>
 
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span>(<span class="hljs-params">B</span>):</span>
 &nbsp;<span class="hljs-keyword">pass</span> 


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span>(<span class="hljs-params">A, B</span>):</span>
 &nbsp;<span class="hljs-keyword">pass</span> 


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">D</span>(<span class="hljs-params">C,A</span>):</span>
 &nbsp;<span class="hljs-keyword">pass</span>
 
print(D.mro())</code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">[&lt;<span class="hljs-class"><span class="hljs-keyword">class</span> '<span class="hljs-title">__main__</span>.<span class="hljs-title">D</span>'&gt;,&lt;<span class="hljs-title">class</span> '<span class="hljs-title">__main__</span>.<span class="hljs-title">C</span>'&gt;,&lt;<span class="hljs-title">class</span> '<span class="hljs-title">__main__</span>.<span class="hljs-title">A</span>'&gt;,&lt;<span class="hljs-title">class</span> '<span class="hljs-title">__main__</span>.<span class="hljs-title">B</span>'&gt;,&lt;<span class="hljs-title">class</span> '<span class="hljs-title">object</span>'&gt;]</span></code></pre><p>&nbsp;</p><h2><strong>Method Resolution Order (MRO)</strong></h2><p>&nbsp;</p><p><strong>Method Resolution Order(MRO)</strong> denotes the way a programming language resolves a method or an attribute. It defines the order in which the subclasses are searched when a method is called. First, the method or the attribute is searched within the subclass and then it is searched in its parent class and so on.</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span>:</span>

   <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print</span>(<span class="hljs-params">self</span>):</span>
       print(<span class="hljs-string">"This is vehicle print"</span>)
       
       
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span>(<span class="hljs-params">Vehicle</span>):</span>

   <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print</span>(<span class="hljs-params">self</span>):</span>
       print(<span class="hljs-string">"This is Car print"</span>)
       
       
<span class="hljs-comment">#driver code   </span>
v = Car()
v.print()</code></pre><p>&nbsp;</p><p><strong>output:&nbsp;</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">This <span class="hljs-keyword">is</span> Car <span class="hljs-keyword">print</span></code></pre><p>&nbsp;</p><p>In the above example, the method that is invoked is from the class <strong>Car</strong> but not from class <strong>Vehicle</strong>, and this is due to the Method Resolution Order(MRO). The order of priority that is followed in the above code is- <strong>class Car &nbsp;&gt; class Vehicle</strong>.&nbsp;</p><p>&nbsp;</p><p>if you want to get rid off of this ambiguity and want to call the print() method of base class we can use syntax:- <strong>ClassName.method(object)</strong>. Here binding the class <strong>Car</strong> and class <strong>Vehcile</strong> with <strong>Waganor</strong> class object.&nbsp;</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vehicle</span>:</span>
    
   <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print</span>(<span class="hljs-params">self</span>):</span>
       print(<span class="hljs-string">"This is vehicle print"</span>)
        
        
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span>:</span>
    
   <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print</span>(<span class="hljs-params">self</span>):</span>
       print(<span class="hljs-string">"This is Car print"</span>)
        
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Waganor</span>(<span class="hljs-params">Car, Vehicle</span>):</span>
    
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">print</span>(<span class="hljs-params">self</span>):</span>
        print(<span class="hljs-string">"This is Waganor print"</span>)
        
        
        
<span class="hljs-comment">#Driver's code</span>
w = Waganor()
w.print()
Car.print(w)
Vehicle.print(w)</code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">This <span class="hljs-keyword">is</span> Waganor <span class="hljs-keyword">print</span>
This <span class="hljs-keyword">is</span> Car <span class="hljs-keyword">print</span>
This <span class="hljs-keyword">is</span> vehicle <span class="hljs-keyword">print</span></code></pre></div></div>