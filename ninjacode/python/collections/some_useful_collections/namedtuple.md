<div _ngcontent-serverapp-c231="" class="note-body"><div _ngcontent-serverapp-c231="" class="body-text"><h2><strong>NamedTuple</strong></h2><p>&nbsp;</p><p>A NamedTuple is a function for tuples with <strong>Named Fields</strong> and can be seen as an extension of the built-in tuple data type. Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code and return a tuple object with names for each position which the ordinary tuples lack. For example, consider a tuple names of books where the first element represents the book's name, second represents the author's name and the third element represents the number of pages in the book. Suppose for calling book name instead of remembering the index position you can actually call the element by using the name argument, then it will be really easy for accessing tuples element. This functionality is provided by the NamedTuple.</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">collections</span>.<span class="hljs-title">namedtuple</span>(<span class="hljs-params">typename, field_names</span>)</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">
<span class="hljs-comment"># Python code to demonstrate namedtuple() </span>

<span class="hljs-keyword">from</span> collections <span class="hljs-keyword">import</span> namedtuple 

<span class="hljs-comment"># Declaring namedtuple() </span>
Book = namedtuple(<span class="hljs-string">'Book'</span>,[<span class="hljs-string">'name'</span>,<span class="hljs-string">'author'</span>,<span class="hljs-string">'pages'</span>]) 

<span class="hljs-comment"># Adding values </span>
book = Book(<span class="hljs-string">'Clean Code'</span>,<span class="hljs-string">'Robert Cecil Martin'</span>,<span class="hljs-string">'431'</span>) 

<span class="hljs-comment"># Access using index </span>
<span class="hljs-keyword">print</span> (<span class="hljs-string">"Getting the Book's author using index : "</span>,end =<span class="hljs-string">""</span>) 
<span class="hljs-keyword">print</span> (book[<span class="hljs-number">1</span>]) 

<span class="hljs-comment"># Access using name </span>
<span class="hljs-keyword">print</span> (<span class="hljs-string">"The Book's name using keyname : "</span>,end =<span class="hljs-string">""</span>) 
<span class="hljs-keyword">print</span> (book.name)
</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Getting the Book<span class="hljs-string">'s author using index : Robert Cecil Martin                                                                  
The Book'</span>s name using keyname : Clean Code</code></pre><p>&nbsp;</p><p><strong>Conversion Operations</strong>&nbsp;</p><p><strong>1. _make():</strong> This function is used to return a namedtuple() from the iterable passed as argument.</p><p><strong>2. _asdict():</strong> This function returns the OrdereDict() as constructed from the mapped values of namedtuple().</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Python code to demonstrate namedtuple() </span>

<span class="hljs-keyword">from</span> collections <span class="hljs-keyword">import</span> namedtuple 

<span class="hljs-comment"># Declaring namedtuple() </span>
Book = namedtuple(<span class="hljs-string">'Book'</span>,[<span class="hljs-string">'name'</span>,<span class="hljs-string">'author'</span>,<span class="hljs-string">'pages'</span>]) 

<span class="hljs-comment"># Adding values </span>
book = Book(<span class="hljs-string">'Clean Code'</span>,<span class="hljs-string">'Robert Cecil Martin'</span>,<span class="hljs-string">'431'</span>) 

<span class="hljs-comment"># Access using index </span>
<span class="hljs-keyword">print</span> (<span class="hljs-string">"Getting the Book's author using index : "</span>,end =<span class="hljs-string">""</span>) 
<span class="hljs-keyword">print</span> (book[<span class="hljs-number">1</span>]) 

<span class="hljs-comment"># Access using name </span>
<span class="hljs-keyword">print</span> (<span class="hljs-string">"The Book's name using keyname : "</span>,end =<span class="hljs-string">""</span>) 
<span class="hljs-keyword">print</span> (book.name)


<span class="hljs-comment"># Adding values initializing iterable </span>
li = [<span class="hljs-string">'Hatching Twitter'</span>, <span class="hljs-string">'Nick Bilton'</span>, <span class="hljs-string">'320'</span> ] 

<span class="hljs-comment"># initializing dict </span>
di = { <span class="hljs-string">'name'</span> : <span class="hljs-string">"Atomic Habits"</span>, <span class="hljs-string">'author'</span> : <span class="hljs-string">'James Clear'</span> , <span class="hljs-string">'pages'</span> : <span class="hljs-string">'288'</span> } 

<span class="hljs-comment"># using _make() to return namedtuple() </span>
<span class="hljs-keyword">print</span> (<span class="hljs-string">"The namedtuple instance using iterable is : "</span>) 
<span class="hljs-keyword">print</span> (Book._make(li)) 

<span class="hljs-comment"># using _asdict() to return an OrderedDict() </span>
<span class="hljs-keyword">print</span> (<span class="hljs-string">"The OrderedDict instance using namedtuple is : "</span>) 
<span class="hljs-keyword">print</span> (book._asdict())</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">Getting the Book<span class="hljs-string">'s author using index : Robert Cecil Martin                                                                  
The Book'</span>s name using keyname : Clean Code                                                                                   
The namedtuple instance using iterable <span class="hljs-keyword">is</span> :                                                                                  
Book(name=<span class="hljs-string">'Hatching Twitter'</span>, author=<span class="hljs-string">'Nick Bilton'</span>, pages=<span class="hljs-string">'320'</span>)                                                             
The OrderedDict instance using namedtuple <span class="hljs-keyword">is</span> :                                                                               
OrderedDict([(<span class="hljs-string">'name'</span>, <span class="hljs-string">'Clean Code'</span>), (<span class="hljs-string">'author'</span>, <span class="hljs-string">'Robert Cecil Martin'</span>), (<span class="hljs-string">'pages'</span>, <span class="hljs-string">'431'</span>)])  </code></pre></div></div>