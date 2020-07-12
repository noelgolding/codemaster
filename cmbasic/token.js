function trigger_event(value) {
  console.log(value)
}

class Token {
  constructor(type, value, line, column) {
    this.type = type;
    this.value = value;
    this.line = line;
    this.column = column;
  }
}

class BeginToken {
  constructor(value, line, column) {
    super(value, value, line, column)
  }
}

class EndToken {
  constructor(value line, column) {
    super(value, value, line, column)
  }
}

class LineNumberToken {
  constructor(value, line, column) {
    super("LINENO", parseInt(value, 10), line, column)
  }
}

class WholeNumberToken {
  constructor(value, line, column) {
    super("WHOLENUMBER", parseInt(value, 10), line, column)
  }
}

class ActionToken {
  constructor(value, line, column) {
    // RUN, JUMP, SLIDE
    super("ACTION", () => trigger_event(value), line, column)
  }
}

class IfToken {
  constructor(value, line, column) {
    super(value, value, line, column)
  }
}

class ThenToken {
  constructor(value, line, column) {
    super(value, value, line, column)
  }
}

class ElseToken {
  constructor(value, line, column) {
    super(value, value, line, column)
  }
}

class GotoToken {
  constructor(value, line, column) {
    super(value, value, line, column)
  }
}

class LoopToken {
  constructor(value, line, column) {
    super(value, value, line, column)
  }
}

class NpcToken {
  constructor(value, line, column) {
    // GEM or TROLL
    super("NPC", value, line, column)
  }
}

class IndentToken {
  constructor(value, line, column) {
    super("INDENT", value, line, column)
  }
}

class BoolOpToken {
  constructor(value, line, column) {
    super("BOOL_OP", value, line, column)
  }
}

class ColorToken {
  constructor(value, line, column) {
    super("COLOR", value, line, column)
  }
}
