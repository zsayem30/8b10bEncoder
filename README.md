# 8b10bEncoder
This is an extension of a project for ELEC 221: Signals and Systems.
The 8b/10b encoder is a system that transforms a sequence of eight bit inputs into a sequence of ten bit
outputs. The encoder keeps track of the previous running disparity between 0's and 1's in the output
sequence to determine the disparity of the next output. By design, this disparity may only be -1 (to denote
there has been one more 0' than 1' in the previous outputs) or +1 (to denote there has been one more 1'
than 0' in the previous outputs). Although there is no disparity at the beginning of the sequence, the initial
disparity is set to -1.
