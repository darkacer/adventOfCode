console.log(
    [2,44,6,1,9,90].map(e => e.toString()).sort((a,b) => Number(a + b) > Number(b + a) ? -1 : 1).join('')
)
