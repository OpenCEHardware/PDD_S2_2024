package utils_pkg;

typedef enum logic[3:0]{

START  = 4'd0,
IDLE   = 4'd1,
READY  = 4'd2,
FKD_UP = 4'dX
} state_t;

typedef struct packed {

logic [7:0]   header;
logic [3:0]   opcode;
logic [63:0]    data; 
logic [3:0]    error;
state_t     m_state;

} packet_t;




endpackage 