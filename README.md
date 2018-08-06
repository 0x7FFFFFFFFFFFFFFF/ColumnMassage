ColumnMassage
=============

A Sublime Text 3 Plugin which rearranges columns of text to meet you needs.

## Feature

See below demonstration.

![](https://raw.githubusercontent.com/yangshuairocks/ColumnMassage/master/column_massage.gif)

## Shortcuts

This plugin has only one shortcut `Ctrl + Shift + ~`.

## How to use

Let's say we have some a csv file with the following content.

```
20180315225757.png,.png,67445
20180624001029.jpg,.jpg,307811
Edde.png,.png,10490
email address.png,.png,48782
```

We want to arrange the text to this:

```
<li><span class="filename">20180315225757.png</span><span class="extension">.png</span><span class="length">67445</span></li>
<li><span class="filename">20180624001029.jpg</span><span class="extension">.jpg</span><span class="length">307811</span></li>
<li><span class="filename">Edde.png</span><span class="extension">.png</span><span class="length">10490</span></li>
<li><span class="filename">email address.png</span><span class="extension">.png</span><span class="length">48782</span></li>
```

First we select the lines:

![](https://raw.githubusercontent.com/yangshuairocks/ColumnMassage/master/howto_step1_select_all.png)

Then we press `Ctrl + Shift + ~` to invoke `ColumnMassage` command.

![](https://raw.githubusercontent.com/yangshuairocks/ColumnMassage/master/howto_step2_call_column_massage.png)

Now we create a rule to tell the plugin how to manipulate the text.

![](https://raw.githubusercontent.com/yangshuairocks/ColumnMassage/master/howto_step3_create_rule.png)

Press `Enter` and we are done.

![](https://raw.githubusercontent.com/yangshuairocks/ColumnMassage/master/howto_step4_done.png)

## How to read the rule

In the above example, we use the rule `,|||((|||))|||<li><span class="filename">((1))</span><span class="extension">((2))</span><span class="length">((3))</span></li>`.

Here `|||` is the rule delimiter and we should not change it. So the rule was separated into 4 parts.

- `,`
  This is the text column delimiter and will be converted into a Python regular expression. In the above example we are using csv syntax, so we specify `,` as the delimiter. Common column delimiters are `\t+`, `\s{2,}`, `\s+` etc.
- `((`
  This is the text that denotes the left side of a column template. See below.
- `))`
  This is the text that denotes the right side of a column template. See below.
- `<li><span class="filename">((1))</span><span class="extension">((2))</span><span class="length">((3))</span></li>`
  This part is the actual rule. You can use column templates in it. A column template looks like `<left_string><column_number><right_string>`. In our example, `<left_string>` is `((` and `<right_string>` is `))`. Except the column templates, other parts of the rule will be inserted literally without any change. 

## Installation

Clone this repository into Sublime Text "Packages" directory.

## License

Yang Shuai
