function multiply()
{
    a = Number(document.getElementById('quantity').value);
    b = Number(document.getElementById('p').value);
    c = a * b;

    document.getElementById('TOTAL').value = c;
}
