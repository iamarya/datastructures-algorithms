<div _ngcontent-serverapp-c232="" class="note-body"><div _ngcontent-serverapp-c232="" class="body-text"><h2><strong>Abstract Classes</strong></h2><p>&nbsp;</p><p>Abstraction is the process of hiding implementation details and only revealing the parts of information which are relevant to the user i.e. it is basically, hiding the unnecessary details from the users. An abstract class can be considered as a blueprint for other classes that it can follow. Abstract classes are those type of classes that can contain one or more abstract methods. Here, an abstract method is a method that has a declaration but does not have an implementation (which is left for the inherited class to implement in its own form/fashion). This set of methods must be created within any child classes which inherit from the abstract class. A class that contains one or more abstract methods is called an <strong>abstract class.</strong></p><h2>&nbsp;</h2><h2><strong>Creating Abstract Classes in Python</strong></h2><p><br>&nbsp;</p><p>● By default, Python does not provide abstract classes.</p><p>&nbsp;</p><p>● Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is <strong>abc</strong>.</p><p>&nbsp;</p><p>● abc works by decorating methods of the base class as abstract and then registering concrete classes as implementations of the abstract base.</p><p>&nbsp;</p><p>● A method becomes abstract when decorated with the keyword <strong>@abstractmethod.</strong></p><p>&nbsp;</p><p>● You are required to import <strong>ABC</strong> superclass and <strong>abstractmethod</strong> from the <strong>abc </strong>module before declaring your abstract class.</p><p>&nbsp;</p><p>● An abstract class cannot be directly instantiated i.e. we cannot create an object of the abstract class.</p><p>&nbsp;</p><p>● However, the subclasses of an abstract class that have definitions for all the abstract methods declared in the abstract class, can be instantiated.</p><p>&nbsp;</p><p>● While declaring abstract methods in the class, it is not mandatory to use the <strong>@abstractmethod </strong>decorator (i.e it would not throw an exception). However, it is considered a good practice to use it as it notifies the compiler that the user has defined an abstract method.</p><p><br>The given Python code uses the <strong>ABC</strong> class and defines an abstract base class:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-keyword">from</span> abc <span class="hljs-keyword">import</span> ABC, abstractmethod <span class="hljs-comment">#Importing the ABC Module</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AbstractClass</span>(<span class="hljs-params">ABC</span>):</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">__init__</span>(<span class="hljs-params">self, value</span>):</span> <span class="hljs-comment">#Class Constructor</span>
        self.value = value
        <span class="hljs-keyword">pass</span>
    
<span class="hljs-meta">    @abstractmethod</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">do_something</span>(<span class="hljs-params">self</span>):</span> <span class="hljs-comment">#Our abstract method declaration</span>
        <span class="hljs-keyword">pass</span></code></pre><p>&nbsp;</p><p>● You are required to define (implement) all the abstract methods declared in an Abstract class, in all its subclasses to be able to instantiate the subclass.</p><p>&nbsp;</p><p><strong>For example</strong>, We will now define a subclass using the previously defined abstract class. You will notice that since we haven't implemented the <strong>do_something</strong> method, in this subclass, we will get an exception.</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestClass</span>(<span class="hljs-params">AbstractClass</span>):</span>
 &nbsp;&nbsp;<span class="hljs-keyword">pass</span> <span class="hljs-comment">#No definition for do_something method </span>

x = TestClass(<span class="hljs-number">4</span>)</code></pre><p><br>We will get the output as:</p><p>&nbsp;</p><pre><code class="language-python hljs">TypeError: Can<span class="hljs-string">'t instantiate abstract class TestClass with abstract methods do_something</span></code></pre><p>&nbsp;</p><p>We will do it the correct way in the following example, in which we define two classes inheriting from our abstract class:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">add</span>(<span class="hljs-params">AbstractClass</span>):</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">do_something</span>(<span class="hljs-params">self</span>):</span>
        <span class="hljs-keyword">return</span> self.value + <span class="hljs-number">42</span>
    

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">mul</span>(<span class="hljs-params">AbstractClass</span>):</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">do_something</span>(<span class="hljs-params">self</span>):</span>
        <span class="hljs-keyword">return</span> self.value * <span class="hljs-number">42</span>


<span class="hljs-comment">#Driver's code</span>
x = add(<span class="hljs-number">10</span>)
y = mul(<span class="hljs-number">10</span>)
print(x.do_something())
print(y.do_something())</code></pre><p>&nbsp;</p><p>We get the output as:</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-number">52</span> 
<span class="hljs-number">420</span></code></pre><p><br>Thus, we can observe that a class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are overridden.&nbsp;</p><p><br>&nbsp;</p><p><strong>Note:</strong> Concrete classes contain only concrete (normal) methods whereas abstract classes may contain both concrete methods and abstract methods.</p><p>&nbsp;</p><p>● An abstract method can have an implementation in the abstract class.&nbsp;</p><p>&nbsp;</p><p>● However, even if they are implemented, this implementation shall be overridden in the subclasses.&nbsp;</p><p>&nbsp;</p><p>● If you wish to invoke the method definition from the abstract superclass, the abstract method can be invoked with super() call mechanism. (Similar to cases of “normal” inheritance).</p><p>&nbsp;</p><p>● Similarly, we can even have concrete methods in the abstract class that can be invoked using super() call. Since these methods are not abstract it is not necessary to provide their implementation in the subclasses.&nbsp;</p><p>&nbsp;</p><p>● Consider the given example:</p><p>&nbsp;</p><p>Let's take an example of an abstract class <i>Payment</i>. It has an abstract method called, <i>paymentMode</i>. There are three classes derived from <i>Payment, </i>namely <i>CreditCardPayment, DebitCardPayment</i>,<i> and UPI_Payment.</i> All the three derived classes implement the abstract method <i>paymentMode</i> as one of their functionalities.</p><p>&nbsp;</p><p>As a user, we are abstracted from the paymentMode that is inside the class <i><strong>Payment</strong></i>. If we are creating another class <i><strong>CreditCardPayment</strong></i> that inherits the properties of class <i><strong>Payment</strong></i> then we must have to override all the abstract methods i.e paymentMethod here.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-keyword">from</span> abc <span class="hljs-keyword">import</span> ABC, abstractmethod

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Payment</span>(<span class="hljs-params">ABC</span>):</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">printSlip</span>(<span class="hljs-params">self, amount</span>):</span>
        print(<span class="hljs-string">'Purchase of amount- '</span>, amount)
   
<span class="hljs-meta">    @abstractmethod</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">paymentMode</span>(<span class="hljs-params">self, amount</span>):</span>
        <span class="hljs-keyword">pass</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CreditCardPayment</span>(<span class="hljs-params">Payment</span>):</span>

    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">paymentMode</span>(<span class="hljs-params">self, amount</span>):</span>
        print(<span class="hljs-string">'Credit card payment of- '</span>, amount)

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DebitCardPayment</span>(<span class="hljs-params">Payment</span>):</span>

    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">paymentMode</span>(<span class="hljs-params">self, amount</span>):</span>
        print(<span class="hljs-string">'Debit card payment of- '</span>, amount)
   
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UPI_Payment</span>(<span class="hljs-params">Payment</span>):</span>

    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">paymentMode</span>(<span class="hljs-params">self,amount</span>):</span>
        print(<span class="hljs-string">"UPI payment of- "</span>,amount)
       
       
       
<span class="hljs-comment">#Driver's code        </span>
object = CreditCardPayment()
object.paymentMode(<span class="hljs-number">100</span>)
object.printSlip(<span class="hljs-number">100</span>)

object = DebitCardPayment()
object.paymentMode(<span class="hljs-number">200</span>)
object.printSlip(<span class="hljs-number">200</span>)

object = UPI_Payment()
object.paymentMode(<span class="hljs-number">300</span>)
object.printSlip(<span class="hljs-number">300</span>)</code></pre><p>&nbsp;</p><p><strong>output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Credit card payment of-  <span class="hljs-number">100</span>
Purchase of amount-  <span class="hljs-number">100</span>
Debit card payment of-  <span class="hljs-number">200</span>
Purchase of amount-  <span class="hljs-number">200</span>
UPI payment of-  <span class="hljs-number">300</span>
Purchase of amount-  <span class="hljs-number">300</span></code></pre><p>&nbsp;</p><p>The given code shows another implementation of an abstract class.</p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Python program showing how an abstract class works</span>
<span class="hljs-keyword">from</span> abc <span class="hljs-keyword">import</span> ABC, abstractmethod

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span>(<span class="hljs-params">ABC</span>):</span> <span class="hljs-comment">#Abstract Class</span>
<span class="hljs-meta">    @abstractmethod</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">move</span>(<span class="hljs-params">self</span>):</span>
        <span class="hljs-keyword">pass</span>


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Human</span>(<span class="hljs-params">Animal</span>):</span> <span class="hljs-comment">#Subclass 1</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">move</span>(<span class="hljs-params">self</span>):</span>
        print(<span class="hljs-string">"I can walk and run"</span>)
        
        
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Snake</span>(<span class="hljs-params">Animal</span>):</span> <span class="hljs-comment">#Subclass 2</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">move</span>(<span class="hljs-params">self</span>):</span>
        print(<span class="hljs-string">"I can crawl"</span>)
   
        
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span>(<span class="hljs-params">Animal</span>):</span> <span class="hljs-comment">#Subclass 3</span>
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">move</span>(<span class="hljs-params">self</span>):</span> 
        print(<span class="hljs-string">"I can bark"</span>)
        

        
<span class="hljs-comment"># Driver's code</span>
R = Human()
R.move()
K = Snake()
K.move()
R = Dog()
R.move()</code></pre><p><br>We will get the output as:<br>&nbsp;</p><pre><code class="language-python hljs">I can walk <span class="hljs-keyword">and</span> run
I can crawl
I can bark</code></pre></div></div>