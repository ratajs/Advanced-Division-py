![](https://raw.githubusercontent.com/ratajs/Advanced-Division/master/imgs/icon.svg)

# Advanced-Division-py
### Divide two numbers using recurring decimals

If you have Python installed, you can test this from the command line, such as <code> py AdvDiv.py 1 7</code> or open the <em>AdvDiv-demo.py</em> file.

Import this library using <code>import AdvDiv</code>

Syntax:
<code>AdvDiv.div(n1, n2, minstr, decstr, str1, rstr2)</code>
* n1 – the first number
* n2 – the second number
* minstr – string representing the minus sign (default "-")
* decstr – string separating the decimal digits (default ".")
* rstr1 – string of the recursion beginning (default "[")
* rstr2 – string of the recursion end (default "]")
## Examples:
<code>print(AdvDiv.div("1", "6"))</code>

<pre>0.1[6]</pre>

<code>print(AdvDiv.div("1", "7"))</code>

<pre>0.[142857]</pre>

<code>print(AdvDiv.div("123.1[24]", "7.54"))</code>

<pre>16.[329475122578570854432923398440639819950164777750984647536371674302708785467406157061]</pre>

This code was created as a translation of my JavaScript [library](https://github.com/ratajs/Advanced-Division-js), so it should produce the same results.
Learn more: <https://advdiv.ratajs.cz>
