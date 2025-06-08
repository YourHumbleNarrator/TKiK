CodeMirror.defineSimpleMode("mylang", {
  start: [
    {regex: /!!-.+?-!!/, token: "comment"},
    {regex: /!![^\n]*/, token: "comment"},

    {regex: /"(?:[^\\"$;,]|\\[nt\\'\";])*"/, token: "string"},
    {regex: /'(?:\\[nt\\'"\\]|[^'\\])'/, token: "string"},
    {regex: /\b[0-9]+\.[0-9]+\b/, token: "number"},
    {regex: /\b[0-9]+\b/, token: "number"},
    {regex: /\b(Piccolo|Intero|Flottante|Doppio|Grande|Carattere|Booleano)\b/, token: "variable-2"},
    {regex: /\b(Vero|Falso)\b/, token: "atom"},
    {regex: /\b(Funzione|inizio|fine|se|allora|fai|altrimenti|per|a'|mentre|continua|ferma|ritorna|principale|no|Scriviere|Caricare)\b/, token: "keyword"},
    {regex: /(:=|\+|\-|\*|\/|%|=|<=|>=|!=|>|<|\|\||&&|\||&|>>|<<|\^|e'|o'|non)/, token: "operator"},

    {regex: /[()\[\],;]/, token: "bracket"},
    {regex: /\$/, token: "variable-3"},
    {regex: /[a-z_][a-zA-Z0-9_]*/, token: "variable"},
  ],
  meta: {
    lineComment: "!!"
  }
});