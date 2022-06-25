let count=0

function inception()
{
    debugger;
    if(count>3)
    {
        return 'doine';
    }
    count++
    inception();
}