import utils_pkg::*;

module tb();

timeunit 1ns;
timeprecision 1ps;
parameter DEPTH = 16; 
parameter COUNT_SIZE = (DEPTH == 0) ? 1 : $clog2(DEPTH); 
logic aclk;
logic resetn;
logic push;
logic pop;
logic [COUNT_SIZE-1:0] wr_ptr;
logic [COUNT_SIZE-1:0] rd_ptr;
logic full;
logic empty;
packet_t input_packet;
packet_t output_packet;


generic_fifo 
#(
.DEPTH(DEPTH),
.COUNT_SIZE(COUNT_SIZE)
)
m_generic_fifo
(
.aclk(aclk),
.resetn(resetn),
.push(push),
.pop(pop),
.wr_ptr(wr_ptr),
.rd_ptr(rd_ptr),
.full(full),
.empty(empty),
.data_in(input_packet),
.data_out(output_packet)
);

initial begin

clk_gen();

end

//test body
initial begin
   packet_t a_packet;
   reset(50, 100);
   #300;//wait for some time
   repeat(12) begin
      a_packet.header = 8'hFF;
      a_packet.opcode = 4'hA;
      a_packet.data   = 64'hDEAF_DEAD_DEAF_DEAD;
      a_packet.error  = 4'hE;
      a_packet.m_state = state_t'($urandom_range(0,4));
      set_input(a_packet);
    end
    repeat(5) begin
      get_output(a_packet);
      $display("wr_ptr = %0d | rd_ptr = %0d |  packet = %p @%t", wr_ptr, rd_ptr, a_packet, $realtime);
    end
    repeat(10) begin
      a_packet.header = 8'hAA;
      a_packet.opcode = 4'hB;
      a_packet.data   = 64'h000_DEAD_DEAF_0000;
      a_packet.error  = 4'hC;
      a_packet.m_state = state_t'($urandom_range(1,2));
      set_input(a_packet);
    end
    repeat(5) begin
      get_output(a_packet);
      $display("wr_ptr = %0d | rd_ptr = %0d |  packet = %p @%t", wr_ptr, rd_ptr, a_packet, $realtime);
    end
end

task clk_gen();

aclk = 0;

forever begin
   #50 aclk = ~aclk;
end

endtask

task reset(int start = 0, int duration =  10);

#start begin
   resetn = 1'b0;
end

#duration begin
   resetn = 1'b1;
end

endtask

task  set_input(input packet_t m_packet);
   @(posedge aclk);
   push         <= 1'b1;
   input_packet <=  m_packet;
   @(posedge aclk);
   push         <= 1'b0;
   repeat (5) @(posedge aclk);
endtask

task get_output(output packet_t m_packet);
   @(posedge aclk);
   pop      <= 1'b1;
   m_packet <= output_packet;
   @(posedge aclk);
   pop      <= 1'b0;
   repeat (5) @(posedge aclk);   
endtask


endmodule
