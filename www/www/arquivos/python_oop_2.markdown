### Criar uma nova classe

Code:

```
$Parsedown = new Parsedown();

echo $Parsedown->text('Hello _Parsedown_!'); # prints: <p>Hello <em>Parsedown</em>!</p>
```