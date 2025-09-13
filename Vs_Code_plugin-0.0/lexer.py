# lexer.py - ENHANCED FOR SYSTEMS PROGRAMMING + TYPE FUSION
from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional, Union, Any, Tuple
import re

class TokenType(Enum):
    # Control Flow Keywords
    RUNTASK = auto()
    PRINTMESSAGE = auto()
    RETURNVALUE = auto()
    IFCONDITION = auto()
    THENBLOCK = auto()
    ELSEBLOCK = auto()
    CHOOSEPATH = auto()
    CASEOPTION = auto()
    DEFAULTOPTION = auto()
    WHILELOOP = auto()
    UNTILCONDITION = auto()
    FOREVERY = auto()
    IN = auto()
    TRYBLOCK = auto()
    CATCHERROR = auto()
    FINALLYBLOCK = auto()
    SENDMESSAGE = auto()
    RECEIVEMESSAGE = auto()
    EVERYINTERVAL = auto()
    BREAKLOOP = auto()
    HALTPROGRAM = auto()
    CONTINUELOOP = auto()
    
    # Pool Types
    FIXEDPOOL = auto()
    DYNAMICPOOL = auto()
    TEMPORALPOOL = auto()
    NEURALPOOL = auto()
    KERNELPOOL = auto()
    ACTORPOOL = auto()
    SECURITYPOOL = auto()
    CONSTRAINEDPOOL = auto()
    FILEPOOL = auto()
    
    # Pool Operations
    SUBPOOL = auto()
    INITIALIZE = auto()
    CANCHANGE = auto()
    CANBENULL = auto()
    RANGE = auto()
    MAXIMUMLENGTH = auto()
    MINIMUMLENGTH = auto()
    ELEMENTTYPE = auto()
    WHERE = auto()
    
    # Math Operators (Named)
    ADD = auto()
    SUBTRACT = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    POWER = auto()
    MODULO = auto()
    SQUAREROOT = auto()
    ABSOLUTEVALUE = auto()
    
    # Comparison Operators (Named)
    GREATERTHAN = auto()
    LESSTHAN = auto()
    GREATEREQUAL = auto()
    LESSEQUAL = auto()
    EQUALTO = auto()
    NOTEQUAL = auto()
    
    # Logical Operators (Named)
    AND = auto()
    OR = auto()
    NOT = auto()
    XOR = auto()
    IMPLIES = auto()
    
    # Bitwise Operators (Named)
    BITWISEAND = auto()
    BITWISEOR = auto()
    BITWISEXOR = auto()
    BITWISENOT = auto()
    LEFTSHIFT = auto()
    RIGHTSHIFT = auto()
    
    # Interactive Input Functions
    READINPUT = auto()
    READINPUTNUMBER = auto()
    GETUSERCHOICE = auto()
    READKEY = auto()
    
    # String Comparison Functions
    STRINGEQUALS = auto()
    STRINGCONTAINS = auto()
    STRINGSTARTSWITH = auto()
    STRINGENDSWITH = auto()
    STRINGCOMPARE = auto()
    
    # String Manipulation Functions
    STRINGCONCAT = auto()
    STRINGLENGTH = auto()
    STRINGSUBSTRING = auto()
    STRINGTOUPPER = auto()
    STRINGTOLOWER = auto()
    STRINGTRIM = auto()
    STRINGREPLACE = auto()
    STRINGTOSTRING = auto()
    NUMBERTOSTRING = auto()
    STRINGTONUMBER = auto()

    # === FILE I/O OPERATIONS ===
    OPENFILE = auto()
    CLOSEFILE = auto()
    READFILE = auto()
    WRITEFILE = auto()
    CREATEFILE = auto()
    DELETEFILE = auto()
    READLINE = auto()
    WRITELINE = auto()
    READTEXTFILE = auto()
    WRITETEXTFILE = auto()
    APPENDTEXTFILE = auto()
    READBINARYFILE = auto()
    WRITEBINARYFILE = auto()
    APPENDBINARYFILE = auto()
    FILEEXISTS = auto()
    GETFILESIZE = auto()
    GETFILEDATE = auto()
    SETFILEDATE = auto()
    GETFILEPERMISSIONS = auto()
    SETFILEPERMISSIONS = auto()
    SEEKPOSITION = auto()
    GETPOSITION = auto()
    REWIND = auto()
    COPYFILE = auto()
    MOVEFILE = auto()
    RENAMEFILE = auto()
    FLUSHFILE = auto()
    LOCKFILE = auto()
    UNLOCKFILE = auto()
    CREATEDIRECTORY = auto()
    DELETEDIRECTORY = auto()
    LISTDIRECTORY = auto()
    DIRECTORYEXISTS = auto()
    GETWORKINGDIRECTORY = auto()
    SETWORKINGDIRECTORY = auto()
    BUFFEREDREAD = auto()
    BUFFEREDWRITE = auto()
    SETBUFFERSIZE = auto()
    FLUSHBUFFERS = auto()

    # === NEW: LOW-LEVEL SYSTEMS PROGRAMMING TOKENS ===
    
    # Memory and Pointer Operations
    POINTER = auto()                    
    DEREFERENCE = auto()               
    ADDRESSOF = auto()                 
    SIZEOF = auto()                    
    ALLOCATE = auto()                  
    DEALLOCATE = auto()                
    MEMORYCOPY = auto()                
    MEMORYSET = auto()                 
    MEMORYCOMPARE = auto()             
    
    # Hardware Register Access
    HARDWAREREGISTER = auto()          
    CONTROLREGISTER = auto()           
    SEGMENTREGISTER = auto()           
    FLAGSREGISTER = auto()             
    MODELSPECIFICREGISTER = auto()     
    
    # Port I/O Operations
    PORTREAD = auto()                  
    PORTWRITE = auto()                 
    PORTREADBYTE = auto()              
    PORTWRITEBYTE = auto()             
    PORTREADWORD = auto()              
    PORTWRITEWORD = auto()             
    PORTREADDWORD = auto()             
    PORTWRITEDWORD = auto()            
    
    # Interrupt and Exception Handling
    INTERRUPTHANDLER = auto()          
    EXCEPTIONHANDLER = auto()          
    ENABLEINTERRUPTS = auto()          
    DISABLEINTERRUPTS = auto()         
    HALT = auto()                      
    WAIT = auto()                      
    TRIGGERSOFTWAREINTERRUPT = auto()  
    INTERRUPTVECTOR = auto()           
    
    # Atomic Operations
    ATOMICREAD = auto()                
    ATOMICWRITE = auto()               
    ATOMICADD = auto()                 
    ATOMICSUBTRACT = auto()            
    ATOMICCOMPARESWAP = auto()         
    ATOMICEXCHANGE = auto()            
    COMPILERFENCE = auto()             
    
    # Cache and Memory Management
    CACHEINVALIDATE = auto()           
    CACHEFLUSH = auto()                
    TLBINVALIDATE = auto()             
    TLBFLUSH = auto()                  
    PHYSICALMEMORY = auto()            
    
    # Inline Assembly
    INLINEASSEMBLY = auto()            
    ASSEMBLY = auto()                  
    VOLATILE = auto()                  
    BARRIER = auto()                   
    
    # System Calls and Kernel Operations
    SYSTEMCALL = auto()                
    PRIVILEGELEVEL = auto()            
    TASKSWITCH = auto()                
    PROCESSCONTEXT = auto()            
    
    # Device Driver Operations
    DEVICEDRIVER = auto()              
    DEVICEREGISTER = auto()            
    DMAOPERATION = auto()              
    MMIOREAD = auto()                  
    MMIOWRITE = auto()                 
    DEVICEINTERRUPT = auto()           
    
    # Boot and Initialization
    BOOTLOADER = auto()                
    KERNELENTRY = auto()               
    INITIALIZATION = auto()            
    GLOBALCONSTRUCTORS = auto()        
    GLOBALDESTRUCTORS = auto()         

   
    # === VIRTUAL MEMORY TOKENS ===
    PAGETABLE = auto()              
    VIRTUALMEMORY = auto()          
    MMIO = auto()                   
    CACHE = auto()                  
    TLB = auto()                    
    MEMORYBARRIER = auto()          

    # Memory Management Flags
    READONLY = auto()               
    READWRITE = auto()              
    READEXECUTE = auto()            
    READWRITEEXECUTE = auto()       
    USERMODE = auto()               
    KERNELMODE = auto()             
    GLOBAL = auto()                 
    DIRTY = auto()                  
    ACCESSED = auto()               

    # Cache Types and Levels
    CACHED = auto()                 
    UNCACHED = auto()               
    WRITECOMBINING = auto()         
    WRITETHROUGH = auto()           
    WRITEBACK = auto()              
    L1CACHE = auto()                
    L2CACHE = auto()                
    L3CACHE = auto()                

    # Page Sizes
    PAGESIZE4KB = auto()            
    PAGESIZE2MB = auto()            
    PAGESIZE1GB = auto()            

    # TLB Operations
    INVALIDATE = auto()             
    FLUSH = auto()                  
    FLUSHALL = auto()               
    FLUSHGLOBAL = auto()            

    # === NEW: TYPE FUSION TOKEN ===
    FUSEDTYPE = auto()              # For fused type identifiers like AddInt32+SIMD

    # Lambda/Function Keywords
    FUNCTION = auto()
    LAMBDA = auto()
    APPLY = auto()
    COMBINATOR = auto()
    INPUT = auto()
    OUTPUT = auto()
    BODY = auto()
    CURRY = auto()
    UNCURRY = auto()
    COMPOSE = auto()
    
    # Type Keywords
    INTEGER = auto()
    FLOATINGPOINT = auto()
    TEXT = auto()
    BOOLEAN = auto()
    ADDRESS = auto()
    ARRAY = auto()
    MAP = auto()
    TUPLE = auto()
    RECORD = auto()
    OPTIONALTYPE = auto()
    CONSTRAINEDTYPE = auto()
    ANY = auto()
    VOID = auto()
    
    # === NEW: Low-Level Type Keywords ===
    BYTE = auto()                      
    WORD = auto()                      
    DWORD = auto()                     
    QWORD = auto()                     
    UINT8 = auto()                     
    UINT16 = auto()                    
    UINT32 = auto()                    
    UINT64 = auto()                    
    INT8 = auto()                      
    INT16 = auto()                     
    INT32 = auto()                     
    INT64 = auto()                     
    
    # Macro Keywords
    MACROBLOCK = auto()
    MACRO = auto()
    RUNMACRO = auto()
    EXPANDMACRO = auto()
    
    # Security Keywords
    SECURITYCONTEXT = auto()
    WITHSECURITY = auto()
    ALLOWEDOPERATIONS = auto()
    DENIEDOPERATIONS = auto()
    MEMORYLIMIT = auto()
    CPUQUOTA = auto()
    LEVEL = auto()
    
    # System/Hardware Keywords
    HARDWARE = auto()
    SYSCALL = auto()
    INTERRUPT = auto()
    REGISTER = auto()
    MEMORY = auto()
    PHYSICALADDRESS = auto()
    VIRTUALADDRESS = auto()
    FLAGS = auto()
    
    # Code Organization
    SUBROUTINE = auto()
    LIBRARYIMPORT = auto()
    LOOPMAIN = auto()
    LOOPACTOR = auto()
    LOOPSTART = auto()
    LOOPEND = auto()
    LOOPSHADOW = auto()
    
    # Constants/Values
    TRUE = auto()
    FALSE = auto()
    NULL = auto()
    AUTOMATIC = auto()
    UNLIMITED = auto()
    
    # Mathematical Constants
    CONSTANT = auto()
    PI = auto()
    E = auto()
    PHI = auto()
    
    # Units
    BYTES = auto()
    KILOBYTES = auto()
    MEGABYTES = auto()
    GIGABYTES = auto()
    SECONDS = auto()
    MILLISECONDS = auto()
    MICROSECONDS = auto()
    PERCENT = auto()
    
    # Delimiters
    DOT = auto()
    LBRACE = auto()
    RBRACE = auto()
    LPAREN = auto()
    RPAREN = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    COMMA = auto()
    COLON = auto()
    SEMICOLON = auto()
    DASH = auto()
    EQUALS = auto()
    
    # Data Flow Operators
    ARROW_RIGHT = auto()      
    ARROW_LEFT = auto()       
    ARROW_BIDIRECTIONAL = auto()  
    
    # Literals
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()
    
    # Comments
    COMMENT = auto()
    DOC_COMMENT = auto()
    COM_COMMENT = auto()
    TAG_COMMENT = auto()
    
    # Special
    EOF = auto()
    NEWLINE = auto()
    
    # Error token
    ERROR = auto()

@dataclass
class Token:
    type: TokenType
    value: Any
    line: int
    column: int
    length: int = 1

class LexerError(Exception):
    def __init__(self, message: str, line: int, column: int):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(f"Lexer error at line {line}, column {column}: {message}")

class TypeFusionRecognizer:
    """Handles recognition of type fusion patterns"""
    
    def __init__(self):
        # Base operations that can be fused
        self.operations = {
            'Add', 'Subtract', 'Multiply', 'Divide', 'Power', 'Modulo',
            'VectorDot', 'VectorCross', 'VectorAdd', 'VectorSubtract',
            'MatrixMultiply', 'MatrixAdd', 'MatrixSubtract', 'MatrixInvert',
            'MemoryCopy', 'MemorySet', 'MemoryCompare',
            'PortRead', 'PortWrite', 'RegisterRead', 'RegisterWrite',
            'AtomicAdd', 'AtomicSubtract', 'AtomicCompareSwap',
            'CacheFlush', 'TLBInvalidate', 'PageTableMap'
        }
        
        # Base types that can be fused
        self.types = {
            'Int8', 'Int16', 'Int32', 'Int64', 'Int128',
            'UInt8', 'UInt16', 'UInt32', 'UInt64', 'UInt128',
            'Float16', 'Float32', 'Float64', 'Float128',
            'Bool', 'Char', 'Address', 'Pointer'
        }
        
        # Modifiers that can be added
        self.speed_modifiers = {'Fast', 'Precise', 'Approximate'}
        self.parallel_modifiers = {'SIMD', 'Parallel', 'Sequential', 'Vectorized', 'Unroll2', 'Unroll4', 'Unroll8'}
        self.memory_modifiers = {'Aligned', 'Aligned16', 'Aligned32', 'Aligned64', 'Cached', 'Temporal', 'Volatile'}
        self.safety_modifiers = {'Checked', 'Unchecked', 'Saturating', 'Throwing'}
        self.algorithm_modifiers = {'Blocked', 'Recursive', 'Iterative', 'Streaming'}
        
        self.all_modifiers = (self.speed_modifiers | self.parallel_modifiers | 
                             self.memory_modifiers | self.safety_modifiers | 
                             self.algorithm_modifiers)
        
        # Pool type patterns
        self.pool_types = {'Fixed', 'Dynamic', 'Temporal'}
    
    def is_valid_fusion_pattern(self, identifier: str) -> bool:
        """Check if identifier matches type fusion pattern"""
        # Handle pool types: FixedPoolFloat32+Aligned64
        if self.is_pool_fusion(identifier):
            return True
            
        # Handle operation fusion: AddInt32+Saturating  
        return self.is_operation_fusion(identifier)
    
    def is_pool_fusion(self, identifier: str) -> bool:
        """Check for pool fusion patterns like FixedPoolFloat32+Aligned64"""
        if '+' in identifier:
            base, modifiers_str = identifier.split('+', 1)
        else:
            base = identifier
            modifiers_str = ""
        
        # Check for PoolType pattern
        for pool_type in self.pool_types:
            if base.startswith(pool_type + 'Pool'):
                remainder = base[len(pool_type + 'Pool'):]
                if remainder in self.types:
                    return self.validate_modifiers(modifiers_str)
        
        return False
    
    def is_operation_fusion(self, identifier: str) -> bool:
        """Check for operation fusion patterns like AddInt32+SIMD"""
        if '+' in identifier:
            base, modifiers_str = identifier.split('+', 1)
        else:
            base = identifier
            modifiers_str = ""
        
        # Try to match Operation + Type pattern
        for operation in self.operations:
            if base.startswith(operation):
                remainder = base[len(operation):]
                if remainder in self.types:
                    return self.validate_modifiers(modifiers_str)
        
        return False
    
    def validate_modifiers(self, modifiers_str: str) -> bool:
        """Validate modifier chain"""
        if not modifiers_str:
            return True
            
        modifiers = modifiers_str.split('+')
        
        # Maximum 2 modifiers
        if len(modifiers) > 2:
            return False
            
        # All modifiers must be valid
        for modifier in modifiers:
            if modifier not in self.all_modifiers:
                return False
        
        return True
    
    def get_fusion_components(self, identifier: str) -> dict:
        """Extract components from a fused type identifier"""
        if '+' in identifier:
            base, modifiers_str = identifier.split('+', 1)
            modifiers = modifiers_str.split('+')
        else:
            base = identifier
            modifiers = []
        
        # Parse base (operation + type or pool + type)
        result = {'base': base, 'modifiers': modifiers}
        
        # Try pool pattern first
        for pool_type in self.pool_types:
            if base.startswith(pool_type + 'Pool'):
                remainder = base[len(pool_type + 'Pool'):]
                if remainder in self.types:
                    result['pattern'] = 'pool'
                    result['pool_type'] = pool_type
                    result['data_type'] = remainder
                    return result
        
        # Try operation pattern
        for operation in self.operations:
            if base.startswith(operation):
                remainder = base[len(operation):]
                if remainder in self.types:
                    result['pattern'] = 'operation'
                    result['operation'] = operation
                    result['data_type'] = remainder
                    return result
        
        result['pattern'] = 'unknown'
        return result

class Lexer:
    def __init__(self, source: str, strict_mode: bool = True):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
        self.strict_mode = strict_mode
        self.diagnostics = []
        
        # NEW: Initialize type fusion recognizer
        self.fusion_recognizer = TypeFusionRecognizer()
        
        self.keywords = {
            # Original keywords (preserved)
            'RunTask': TokenType.RUNTASK,
            'PrintMessage': TokenType.PRINTMESSAGE,
            'ReturnValue': TokenType.RETURNVALUE,
            'IfCondition': TokenType.IFCONDITION,
            'ThenBlock': TokenType.THENBLOCK,
            'ElseBlock': TokenType.ELSEBLOCK,
            'ChoosePath': TokenType.CHOOSEPATH,
            'CaseOption': TokenType.CASEOPTION,
            'DefaultOption': TokenType.DEFAULTOPTION,
            'WhileLoop': TokenType.WHILELOOP,
            'UntilCondition': TokenType.UNTILCONDITION,
            'ForEvery': TokenType.FOREVERY,
            'in': TokenType.IN,
            'TryBlock': TokenType.TRYBLOCK,
            'CatchError': TokenType.CATCHERROR,
            'FinallyBlock': TokenType.FINALLYBLOCK,
            'SendMessage': TokenType.SENDMESSAGE,
            'ReceiveMessage': TokenType.RECEIVEMESSAGE,
            'EveryInterval': TokenType.EVERYINTERVAL,
            'BreakLoop': TokenType.BREAKLOOP,
            'HaltProgram': TokenType.HALTPROGRAM,
            'ContinueLoop': TokenType.CONTINUELOOP,
            'FixedPool': TokenType.FIXEDPOOL,
            'DynamicPool': TokenType.DYNAMICPOOL,
            'TemporalPool': TokenType.TEMPORALPOOL,
            'NeuralPool': TokenType.NEURALPOOL,
            'KernelPool': TokenType.KERNELPOOL,
            'ActorPool': TokenType.ACTORPOOL,
            'SecurityPool': TokenType.SECURITYPOOL,
            'ConstrainedPool': TokenType.CONSTRAINEDPOOL,
            'FilePool': TokenType.FILEPOOL,
            'SubPool': TokenType.SUBPOOL,
            'Initialize': TokenType.INITIALIZE,
            'CanChange': TokenType.CANCHANGE,
            'CanBeNull': TokenType.CANBENULL,
            'Range': TokenType.RANGE,
            'MaximumLength': TokenType.MAXIMUMLENGTH,
            'MinimumLength': TokenType.MINIMUMLENGTH,
            'ElementType': TokenType.ELEMENTTYPE,
            'Where': TokenType.WHERE,
            'Add': TokenType.ADD,
            'Subtract': TokenType.SUBTRACT,
            'Multiply': TokenType.MULTIPLY,
            'Divide': TokenType.DIVIDE,
            'Power': TokenType.POWER,
            'Modulo': TokenType.MODULO,
            'SquareRoot': TokenType.SQUAREROOT,
            'AbsoluteValue': TokenType.ABSOLUTEVALUE,
            'GreaterThan': TokenType.GREATERTHAN,
            'LessThan': TokenType.LESSTHAN,
            'GreaterEqual': TokenType.GREATEREQUAL,
            'LessEqual': TokenType.LESSEQUAL,
            'EqualTo': TokenType.EQUALTO,
            'NotEqual': TokenType.NOTEQUAL,
            'And': TokenType.AND,
            'Or': TokenType.OR,
            'Not': TokenType.NOT,
            'Xor': TokenType.XOR,
            'Implies': TokenType.IMPLIES,
            'BitwiseAnd': TokenType.BITWISEAND,
            'BitwiseOr': TokenType.BITWISEOR,
            'BitwiseXor': TokenType.BITWISEXOR,
            'BitwiseNot': TokenType.BITWISENOT,
            'LeftShift': TokenType.LEFTSHIFT,
            'RightShift': TokenType.RIGHTSHIFT,
            'Function': TokenType.FUNCTION,
            'Lambda': TokenType.LAMBDA,
            'Apply': TokenType.APPLY,
            'Combinator': TokenType.COMBINATOR,
            'Input': TokenType.INPUT,
            'Output': TokenType.OUTPUT,
            'Body': TokenType.BODY,
            'Curry': TokenType.CURRY,
            'Uncurry': TokenType.UNCURRY,
            'Compose': TokenType.COMPOSE,
            'Integer': TokenType.INTEGER,
            'FloatingPoint': TokenType.FLOATINGPOINT,
            'Text': TokenType.TEXT,
            'Boolean': TokenType.BOOLEAN,
            'Address': TokenType.ADDRESS,
            'Array': TokenType.ARRAY,
            'Map': TokenType.MAP,
            'Tuple': TokenType.TUPLE,
            'Record': TokenType.RECORD,
            'OptionalType': TokenType.OPTIONALTYPE,
            'ConstrainedType': TokenType.CONSTRAINEDTYPE,
            'Any': TokenType.ANY,
            'Void': TokenType.VOID,
            'MacroBlock': TokenType.MACROBLOCK,
            'Macro': TokenType.MACRO,
            'RunMacro': TokenType.RUNMACRO,
            'ExpandMacro': TokenType.EXPANDMACRO,
            'SecurityContext': TokenType.SECURITYCONTEXT,
            'WithSecurity': TokenType.WITHSECURITY,
            'AllowedOperations': TokenType.ALLOWEDOPERATIONS,
            'DeniedOperations': TokenType.DENIEDOPERATIONS,
            'MemoryLimit': TokenType.MEMORYLIMIT,
            'CPUQuota': TokenType.CPUQUOTA,
            'Level': TokenType.LEVEL,
            'Hardware': TokenType.HARDWARE,
            'Syscall': TokenType.SYSCALL,
            'Interrupt': TokenType.INTERRUPT,
            'Register': TokenType.REGISTER,
            'Memory': TokenType.MEMORY,
            'PhysicalAddress': TokenType.PHYSICALADDRESS,
            'VirtualAddress': TokenType.VIRTUALADDRESS,
            'Flags': TokenType.FLAGS,
            'SubRoutine': TokenType.SUBROUTINE,
            'LibraryImport': TokenType.LIBRARYIMPORT,
            'LoopMain': TokenType.LOOPMAIN,
            'LoopActor': TokenType.LOOPACTOR,
            'LoopStart': TokenType.LOOPSTART,
            'LoopEnd': TokenType.LOOPEND,
            'LoopShadow': TokenType.LOOPSHADOW,
            'True': TokenType.TRUE,
            'False': TokenType.FALSE,
            'Null': TokenType.NULL,
            'Automatic': TokenType.AUTOMATIC,
            'Unlimited': TokenType.UNLIMITED,
            'Constant': TokenType.CONSTANT,
            'PI': TokenType.PI,
            'E': TokenType.E,
            'PHI': TokenType.PHI,
            'Bytes': TokenType.BYTES,
            'Kilobytes': TokenType.KILOBYTES,
            'Megabytes': TokenType.MEGABYTES,
            'Gigabytes': TokenType.GIGABYTES,
            'Seconds': TokenType.SECONDS,
            'Milliseconds': TokenType.MILLISECONDS,
            'Microseconds': TokenType.MICROSECONDS,
            'Percent': TokenType.PERCENT,
            
            # String and I/O functions (preserved)
            'ReadInput': TokenType.READINPUT,
            'ReadInputNumber': TokenType.READINPUTNUMBER,
            'GetUserChoice': TokenType.GETUSERCHOICE,
            'ReadKey': TokenType.READKEY,
            'StringEquals': TokenType.STRINGEQUALS,
            'StringContains': TokenType.STRINGCONTAINS,
            'StringStartsWith': TokenType.STRINGSTARTSWITH,
            'StringEndsWith': TokenType.STRINGENDSWITH,
            'StringCompare': TokenType.STRINGCOMPARE,
            'StringConcat': TokenType.STRINGCONCAT,
            'StringLength': TokenType.STRINGLENGTH,
            'StringSubstring': TokenType.STRINGSUBSTRING,
            'StringToUpper': TokenType.STRINGTOUPPER,
            'StringToLower': TokenType.STRINGTOLOWER,
            'StringTrim': TokenType.STRINGTRIM,
            'StringReplace': TokenType.STRINGREPLACE,
            'StringToString': TokenType.STRINGTOSTRING,
            'NumberToString': TokenType.NUMBERTOSTRING,
            'StringToNumber': TokenType.STRINGTONUMBER,
            
            # File I/O (preserved)
            'OpenFile': TokenType.OPENFILE,
            'CloseFile': TokenType.CLOSEFILE,
            'ReadFile': TokenType.READFILE,
            'WriteFile': TokenType.WRITEFILE,
            'CreateFile': TokenType.CREATEFILE,
            'DeleteFile': TokenType.DELETEFILE,
            'ReadLine': TokenType.READLINE,
            'WriteLine': TokenType.WRITELINE,
            'ReadTextFile': TokenType.READTEXTFILE,
            'WriteTextFile': TokenType.WRITETEXTFILE,
            'AppendTextFile': TokenType.APPENDTEXTFILE,
            'ReadBinaryFile': TokenType.READBINARYFILE,
            'WriteBinaryFile': TokenType.WRITEBINARYFILE,
            'AppendBinaryFile': TokenType.APPENDBINARYFILE,
            'FileExists': TokenType.FILEEXISTS,
            'GetFileSize': TokenType.GETFILESIZE,
            'GetFileDate': TokenType.GETFILEDATE,
            'SetFileDate': TokenType.SETFILEDATE,
            'GetFilePermissions': TokenType.GETFILEPERMISSIONS,
            'SetFilePermissions': TokenType.SETFILEPERMISSIONS,
            'SeekPosition': TokenType.SEEKPOSITION,
            'GetPosition': TokenType.GETPOSITION,
            'Rewind': TokenType.REWIND,
            'CopyFile': TokenType.COPYFILE,
            'MoveFile': TokenType.MOVEFILE,
            'RenameFile': TokenType.RENAMEFILE,
            'FlushFile': TokenType.FLUSHFILE,
            'LockFile': TokenType.LOCKFILE,
            'UnlockFile': TokenType.UNLOCKFILE,
            'CreateDirectory': TokenType.CREATEDIRECTORY,
            'DeleteDirectory': TokenType.DELETEDIRECTORY,
            'ListDirectory': TokenType.LISTDIRECTORY,
            'DirectoryExists': TokenType.DIRECTORYEXISTS,
            'GetWorkingDirectory': TokenType.GETWORKINGDIRECTORY,
            'SetWorkingDirectory': TokenType.SETWORKINGDIRECTORY,
            'BufferedRead': TokenType.BUFFEREDREAD,
            'BufferedWrite': TokenType.BUFFEREDWRITE,
            'SetBufferSize': TokenType.SETBUFFERSIZE,
            'FlushBuffers': TokenType.FLUSHBUFFERS,
            
            # === NEW: Low-Level Systems Programming Keywords ===
            
            # Memory and Pointer Operations  
            'Pointer': TokenType.POINTER,
            'Dereference': TokenType.DEREFERENCE,
            'AddressOf': TokenType.ADDRESSOF,
            'SizeOf': TokenType.SIZEOF,
            'Allocate': TokenType.ALLOCATE,
            'Deallocate': TokenType.DEALLOCATE,
            'MemoryCopy': TokenType.MEMORYCOPY,
            'MemorySet': TokenType.MEMORYSET,
            'MemoryCompare': TokenType.MEMORYCOMPARE,
            
            # Hardware Register Access
            'HardwareRegister': TokenType.HARDWAREREGISTER,
            'ControlRegister': TokenType.CONTROLREGISTER,
            'SegmentRegister': TokenType.SEGMENTREGISTER,
            'FlagsRegister': TokenType.FLAGSREGISTER,
            'ModelSpecificRegister': TokenType.MODELSPECIFICREGISTER,
            
            # Port I/O Operations
            'PortRead': TokenType.PORTREAD,
            'PortWrite': TokenType.PORTWRITE,
            'PortReadByte': TokenType.PORTREADBYTE,
            'PortWriteByte': TokenType.PORTWRITEBYTE,
            'PortReadWord': TokenType.PORTREADWORD,
            'PortWriteWord': TokenType.PORTWRITEWORD,
            'PortReadDWord': TokenType.PORTREADDWORD,
            'PortWriteDWord': TokenType.PORTWRITEDWORD,
            
            # Interrupt and Exception Handling
            'InterruptHandler': TokenType.INTERRUPTHANDLER,
            'ExceptionHandler': TokenType.EXCEPTIONHANDLER,
            'EnableInterrupts': TokenType.ENABLEINTERRUPTS,
            'DisableInterrupts': TokenType.DISABLEINTERRUPTS,
            'Halt': TokenType.HALT,
            'Wait': TokenType.WAIT,
            'TriggerSoftwareInterrupt': TokenType.TRIGGERSOFTWAREINTERRUPT,
            'InterruptVector': TokenType.INTERRUPTVECTOR,
            
            # Atomic Operations
            'AtomicRead': TokenType.ATOMICREAD,
            'AtomicWrite': TokenType.ATOMICWRITE,
            'AtomicAdd': TokenType.ATOMICADD,
            'AtomicSubtract': TokenType.ATOMICSUBTRACT,
            'AtomicCompareSwap': TokenType.ATOMICCOMPARESWAP,
            'AtomicExchange': TokenType.ATOMICEXCHANGE,
            'MemoryBarrier': TokenType.MEMORYBARRIER,
            'CompilerFence': TokenType.COMPILERFENCE,
            
            # Cache and Memory Management
            'CacheInvalidate': TokenType.CACHEINVALIDATE,
            'CacheFlush': TokenType.CACHEFLUSH,
            'TLBInvalidate': TokenType.TLBINVALIDATE,
            'TLBFlush': TokenType.TLBFLUSH,
            'PageTable': TokenType.PAGETABLE,
            'PhysicalMemory': TokenType.PHYSICALMEMORY,
            
            # Inline Assembly
            'InlineAssembly': TokenType.INLINEASSEMBLY,
            'Assembly': TokenType.ASSEMBLY,
            'Volatile': TokenType.VOLATILE,
            'Barrier': TokenType.BARRIER,
            
            # System Calls and Kernel Operations
            'SystemCall': TokenType.SYSTEMCALL,
            'PrivilegeLevel': TokenType.PRIVILEGELEVEL,
            'TaskSwitch': TokenType.TASKSWITCH,
            'ProcessContext': TokenType.PROCESSCONTEXT,
            
            # Device Driver Operations
            'DeviceDriver': TokenType.DEVICEDRIVER,
            'DeviceRegister': TokenType.DEVICEREGISTER,
            'DMAOperation': TokenType.DMAOPERATION,
            'MMIORead': TokenType.MMIOREAD,
            'MMIOWrite': TokenType.MMIOWRITE,
            'DeviceInterrupt': TokenType.DEVICEINTERRUPT,
            
            # Boot and Initialization
            'Bootloader': TokenType.BOOTLOADER,
            'KernelEntry': TokenType.KERNELENTRY,
            'Initialization': TokenType.INITIALIZATION,
            'GlobalConstructors': TokenType.GLOBALCONSTRUCTORS,
            'GlobalDestructors': TokenType.GLOBALDESTRUCTORS,
            
            # Low-Level Types
            'Byte': TokenType.BYTE,
            'Word': TokenType.WORD,
            'DWord': TokenType.DWORD,
            'QWord': TokenType.QWORD,
            'UInt8': TokenType.UINT8,
            'UInt16': TokenType.UINT16,
            'UInt32': TokenType.UINT32,
            'UInt64': TokenType.UINT64,
            'Int8': TokenType.INT8,
            'Int16': TokenType.INT16,
            'Int32': TokenType.INT32,
            'Int64': TokenType.INT64,
            
            # === VIRTUAL MEMORY KEYWORDS ===
            
            # Main VM Operations
            'PageTable': TokenType.PAGETABLE,
            'VirtualMemory': TokenType.VIRTUALMEMORY,
            'MMIO': TokenType.MMIO,
            'Cache': TokenType.CACHE,
            'TLB': TokenType.TLB,
            
            
            # Memory Protection Flags
            'ReadOnly': TokenType.READONLY,
            'ReadWrite': TokenType.READWRITE,
            'ReadExecute': TokenType.READEXECUTE,
            'ReadWriteExecute': TokenType.READWRITEEXECUTE,
            'RO': TokenType.READONLY,           
            'RW': TokenType.READWRITE,          
            'RX': TokenType.READEXECUTE,        
            'RWX': TokenType.READWRITEEXECUTE,  
            'UserMode': TokenType.USERMODE,
            'KernelMode': TokenType.KERNELMODE,
            'Global': TokenType.GLOBAL,
            'Dirty': TokenType.DIRTY,
            'Accessed': TokenType.ACCESSED,
            
            # Cache Types
            'Cached': TokenType.CACHED,
            'Uncached': TokenType.UNCACHED,
            'WriteCombining': TokenType.WRITECOMBINING,
            'WriteThrough': TokenType.WRITETHROUGH,
            'WriteBack': TokenType.WRITEBACK,
            
            # Cache Levels
            'L1': TokenType.L1CACHE,
            'L2': TokenType.L2CACHE,
            'L3': TokenType.L3CACHE,
            
            # Page Sizes
            '4KB': TokenType.PAGESIZE4KB,
            '2MB': TokenType.PAGESIZE2MB,
            '1GB': TokenType.PAGESIZE1GB,
            
            # TLB Operations
            'Invalidate': TokenType.INVALIDATE,
            'Flush': TokenType.FLUSH,
            'FlushAll': TokenType.FLUSHALL,
            'FlushGlobal': TokenType.FLUSHGLOBAL,
        }
        
        # Allow short identifiers for systems programming (register names, etc.)
        self.allowed_short_identifiers = {
            'in', 'to', 'by', 'of', 'as', 'is', 'on', 'at', 'PI', 'E', 
            'GRP', 'HW', 'CFG', 'MEM', 'CPU', 'SYS', 'IO', 'RG', 'VG', 
            'PG', 'TG', 'NG', 'KG', 'AG', 'SG', 'CG', 'FG',
            # New: CPU register names
            'EAX', 'EBX', 'ECX', 'EDX', 'ESI', 'EDI', 'ESP', 'EBP',
            'RAX', 'RBX', 'RCX', 'RDX', 'RSI', 'RDI', 'RSP', 'RBP',
            'R8', 'R9', 'R10', 'R11', 'R12', 'R13', 'R14', 'R15',
            'CS', 'DS', 'ES', 'FS', 'GS', 'SS', 'CR0', 'CR1', 'CR2', 
            'CR3', 'CR4', 'CR8', 'DR0', 'DR1', 'DR2', 'DR3', 'DR6', 'DR7'
        }

    def error(self, message: str):
        raise LexerError(message, self.line, self.column)

    def warning(self, message: str):
        # NEW: Collect warnings instead of just printing
        self.diagnostics.append({
            "line": self.line,
            "column": self.column, 
            "message": message,
            "severity": 2  # Warning severity
        })
        # Keep console output for non-LSP usage
        print(f"Warning at line {self.line}, column {self.column}: {message}")

    def current_char(self) -> Optional[str]:
        if self.position >= len(self.source):
            return None
        return self.source[self.position]

    def peek_char(self, offset: int = 1) -> Optional[str]:
        pos = self.position + offset
        if pos >= len(self.source):
            return None
        return self.source[pos]

    def advance(self):
        if self.position < len(self.source):
            if self.source[self.position] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.position += 1

    def skip_whitespace(self):
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()

    def read_string(self) -> str:
        value = ''
        self.advance()
        while self.current_char() and self.current_char() != '"':
            if self.current_char() == '\\':
                self.advance()
                if self.current_char() is None:
                    self.error("Unterminated string escape")
                escape_char = self.current_char()
                if escape_char == 'n':
                    value += '\n'
                elif escape_char == 't':
                    value += '\t'
                elif escape_char == 'r':
                    value += '\r'
                elif escape_char == '"':
                    value += '"'
                elif escape_char == '\\':
                    value += '\\'
                elif escape_char == '0':
                    value += '\0'
                else:
                    self.warning(f"Unknown escape sequence '\\{escape_char}'")
                    value += escape_char
            else:
                value += self.current_char()
            self.advance()
        if self.current_char() == '"':
            self.advance()
        else:
            self.error("Unterminated string literal")
        return value

    def read_number(self) -> Union[int, float]:
        value = ''
        has_dot = False
        if self.current_char() == '0' and self.peek_char() in 'xX':
            self.advance()
            self.advance()
            hex_value = ''
            while self.current_char() and self.current_char() in '0123456789ABCDEFabcdef_':
                if self.current_char() != '_':
                    hex_value += self.current_char()
                self.advance()
            if not hex_value:
                self.error("Invalid hexadecimal literal")
            return int(hex_value, 16)
        while self.current_char() and (self.current_char().isdigit() or self.current_char() in '._'):
            if self.current_char() == '.':
                if has_dot:
                    break
                has_dot = True
                value += '.'
            elif self.current_char() != '_':
                value += self.current_char()
            self.advance()
        if self.current_char() and self.current_char() in 'eE':
            value += self.current_char()
            self.advance()
            if self.current_char() and self.current_char() in '+-':
                value += self.current_char()
                self.advance()
            while self.current_char() and self.current_char().isdigit():
                value += self.current_char()
                self.advance()
        try:
            return float(value) if has_dot or 'e' in value.lower() else int(value)
        except ValueError:
            self.error(f"Invalid number literal: {value}")

    def read_identifier(self) -> str:
        value = ''
        if not (self.current_char().isalpha() or self.current_char() == '_'):
            self.error(f"Identifier must start with letter or underscore, not '{self.current_char()}'")
        while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
            value += self.current_char()
            self.advance()
        
        # Relaxed identifier length checking for systems programming
        if self.strict_mode and len(value) < 3 and value not in self.allowed_short_identifiers:
            self.warning(f"Identifier '{value}' is short - consider using descriptive names for readability")
        
        return value

    def read_fused_identifier(self) -> str:
        """Read a potentially fused identifier with + modifiers"""
        value = ''
        
        # Read the base identifier
        if not (self.current_char().isalpha() or self.current_char() == '_'):
            self.error(f"Identifier must start with letter or underscore, not '{self.current_char()}'")
        
        while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
            value += self.current_char()
            self.advance()
        
        # Check for + modifiers (type fusion)
        while self.current_char() == '+':
            value += self.current_char()
            self.advance()
            
            # Read the modifier
            if not (self.current_char() and self.current_char().isalpha()):
                self.error("Expected modifier after '+' in fused type")
            
            while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
                value += self.current_char()
                self.advance()
        
        return value

    def read_dotted_identifier(self) -> str:
        parts = [self.read_identifier()]
        while self.current_char() == '.':
            if self.peek_char() and self.peek_char().isalpha():
                self.advance()
                parts.append(self.read_identifier())
            else:
                break
        return '.'.join(parts)

    def read_comment(self) -> Tuple[TokenType, str]:
        if self.peek_char() != '/':
            self.error("Invalid comment start")
        self.advance()
        self.advance()
        comment_type = TokenType.COMMENT
        prefix = ''
        if self.current_char() and self.current_char().isalpha():
            while self.current_char() and self.current_char().isalpha():
                prefix += self.current_char()
                self.advance()
            if prefix == 'DOC':
                comment_type = TokenType.DOC_COMMENT
            elif prefix == 'COM':
                comment_type = TokenType.COM_COMMENT
            elif prefix == 'TAG':
                comment_type = TokenType.TAG_COMMENT
            else:
                self.position -= len(prefix)
                self.column -= len(prefix)
                prefix = ''
        if prefix and self.current_char() == ':':
            self.advance()
        while self.current_char() and self.current_char() in ' \t':
            self.advance()
        value = ''
        if comment_type in (TokenType.DOC_COMMENT, TokenType.COM_COMMENT):
            while self.position + 1 < len(self.source):
                if self.source[self.position:self.position+2] == '//':
                    self.advance()
                    self.advance()
                    break
                value += self.current_char()
                self.advance()
        else:
            while self.current_char() and self.current_char() != '\n':
                value += self.current_char()
                self.advance()
        return comment_type, value.strip()

    def tokenize(self) -> List[Token]:
        while self.position < len(self.source):
            self.skip_whitespace()
            if not self.current_char():
                break
            line_start = self.line
            col_start = self.column
            if self.current_char() == '\n':
                self.tokens.append(Token(TokenType.NEWLINE, '\n', line_start, col_start))
                self.advance()
                continue
            if self.current_char() == '/' and self.peek_char() == '/':
                comment_type, value = self.read_comment()
                self.tokens.append(Token(comment_type, value, line_start, col_start))
                continue
            if self.current_char() == '"':
                value = self.read_string()
                self.tokens.append(Token(TokenType.STRING, value, line_start, col_start))
                continue
            if self.current_char().isdigit():
                value = self.read_number()
                self.tokens.append(Token(TokenType.NUMBER, value, line_start, col_start))
                continue
            three_char = self.source[self.position:self.position+3] if self.position + 2 < len(self.source) else ''
            two_char = self.source[self.position:self.position+2] if self.position + 1 < len(self.source) else ''
            if three_char == '<->':
                self.advance()
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.ARROW_BIDIRECTIONAL, '<->', line_start, col_start, 3))
                continue
            elif two_char == '->':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.ARROW_RIGHT, '->', line_start, col_start, 2))
                continue
            elif two_char == '<-':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.ARROW_LEFT, '<-', line_start, col_start, 2))
                continue
            elif two_char == '>=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.GREATEREQUAL, '>=', line_start, col_start, 2))
                continue
            elif two_char == '<=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.LESSEQUAL, '<=', line_start, col_start, 2))
                continue
            elif two_char == '==':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.EQUALTO, '==', line_start, col_start, 2))
                continue
            elif two_char == '!=':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.NOTEQUAL, '!=', line_start, col_start, 2))
                continue
            elif two_char == '&&':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.AND, '&&', line_start, col_start, 2))
                continue
            elif two_char == '||':
                self.advance()
                self.advance()
                self.tokens.append(Token(TokenType.OR, '||', line_start, col_start, 2))
                continue
            single_char_tokens = {
                '=': TokenType.EQUALS,
                '{': TokenType.LBRACE,
                '}': TokenType.RBRACE,
                '(': TokenType.LPAREN,
                ')': TokenType.RPAREN,
                '[': TokenType.LBRACKET,
                ']': TokenType.RBRACKET,
                ',': TokenType.COMMA,
                ':': TokenType.COLON,
                ';': TokenType.SEMICOLON,
                '.': TokenType.DOT,
                '-': TokenType.DASH,
                # ADD THESE PEMDAS OPERATORS:
                '+': TokenType.ADD,
                '*': TokenType.MULTIPLY,
                '/': TokenType.DIVIDE,
                '^': TokenType.POWER,
                '>': TokenType.GREATERTHAN,
                '<': TokenType.LESSTHAN,
                '&': TokenType.AND,
                '|': TokenType.OR,
                '!': TokenType.NOT,
            }
            if self.current_char() in single_char_tokens:
                if self.current_char() == '.' and self.peek_char() and self.peek_char().isalpha():
                    pass
                else:
                    token_type = single_char_tokens[self.current_char()]
                    value = self.current_char()
                    self.advance()
                    self.tokens.append(Token(token_type, value, line_start, col_start, 1))
                    continue
            if self.current_char().isalpha() or self.current_char() == '_':
                # === NEW: TYPE FUSION HANDLING ===
                # Read potentially fused identifier
                value = self.read_fused_identifier()
                
                # Check if it's a valid type fusion pattern
                if self.fusion_recognizer.is_valid_fusion_pattern(value):
                    # It's a fused type! Create a FUSEDTYPE token
                    self.tokens.append(Token(TokenType.FUSEDTYPE, value, line_start, col_start, len(value)))
                    
                    # Log successful fusion recognition
                    components = self.fusion_recognizer.get_fusion_components(value)
                    print(f"✅ TYPE FUSION RECOGNIZED: {value}")
                    print(f"   Pattern: {components.get('pattern', 'unknown')}")
                    if components.get('pattern') == 'operation':
                        print(f"   Operation: {components.get('operation')}, Type: {components.get('data_type')}")
                    elif components.get('pattern') == 'pool':
                        print(f"   Pool: {components.get('pool_type')}, Type: {components.get('data_type')}")
                    if components.get('modifiers'):
                        print(f"   Modifiers: {', '.join(components.get('modifiers'))}")
                    continue
                
                # Check if it's a regular keyword
                token_type = self.keywords.get(value, TokenType.IDENTIFIER)
                
                # If it's a keyword, use it as-is
                if token_type != TokenType.IDENTIFIER:
                    self.tokens.append(Token(token_type, value, line_start, col_start, len(value)))
                    continue
                
                # If it's an identifier, check for dots and continue reading
                if self.current_char() == '.' and self.peek_char() and self.peek_char().isalpha():
                    parts = [value]
                    while self.current_char() == '.' and self.peek_char() and self.peek_char().isalpha():
                        self.advance()  # consume the dot
                        parts.append(self.read_identifier())
                    value = '.'.join(parts)
                
                self.tokens.append(Token(TokenType.IDENTIFIER, value, line_start, col_start, len(value)))
                continue
                
            # Handle dot as a separate token
            if self.current_char() == '.':
                self.advance()
                self.tokens.append(Token(TokenType.DOT, '.', line_start, col_start, 1))
                continue

            self.error(f"Unknown character '{self.current_char()}'")
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens