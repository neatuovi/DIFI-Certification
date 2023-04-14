################
# DIFI Constants
################

DIFI_STANDARD_FLOW_SIGNAL_CONTEXT = 0x4
DIFI_STANDARD_FLOW_SIGNAL_CONTEXT_SIZE = 27
DIFI_VERSION_FLOW_SIGNAL_CONTEXT = 0x5
DIFI_VERSION_FLOW_SIGNAL_CONTEXT_SIZE = 11
DIFI_STANDARD_FLOW_SIGNAL_DATA_WITH_STREAMID = 0x1
DIFI_STANDARD_FLOW_SIGNAL_DATA_NO_STREAMID = 0x0

# class id
DIFI_CLASSID = 0x1 #01

# reserved
DIFI_RESERVED = 0x0 #00

# tsm - data packets
DIFI_TSM_DATA = 0x0 #00
# tsm - standard context / version context
DIFI_TSM_GENERAL_TIMING = 0x1 #01

# tsi
DIFI_TSI_NONE = 0x0  #00
DIFI_TSI_UTC = 0x1   #01 (default, but can be any)
DIFI_TSI_GPS = 0x2   #10
DIFI_TSI_OTHER = 0x3 #11

# tsf
DIFI_TSF_NONE = 0x0 #00
DIFI_TSF_SAMPLE_COUNT = 0x1 #01
DIFI_TSF_REALTIME_PICOSECONDS = 0x2 #10
DIFI_TSF_FREE_RUNNING_COUNT = 0x3 #11

# icc/pcc - version context
DIFI_INFORMATION_CLASS_CODE_VERSION_FLOW_CONTEXT = 0x1 
DIFI_PACKET_CLASS_CODE_VERSION_FLOW_CONTEXT = 0x4 

# cif0/cif1 - standard context
DIFI_CONTEXT_INDICATOR_FIELD_STANDARD_FLOW_CONTEXT = 0xBB98000 #(DIFI must be this, which is ignoring 1st nibble)
# cif0/cif1 - version context
DIFI_CONTEXT_INDICATOR_FIELD_0_VERSION_FLOW_CONTEXT = 0x0000002 #(DIFI must be this, which is ignoring 1st nibble)
DIFI_CONTEXT_INDICATOR_FIELD_1_VERSION_FLOW_CONTEXT = 0x0000000C 

# v49 spec - version context
DIFI_V49_SPEC_VERSION_VERSION_FLOW_CONTEXT = 0x00000004 

# not required for DIFI anymore
#DIFI_REFERENCE_POINT = 0x00000064 

# state/event indicators - standard context
DIFI_STATE_EVENT_IND_FREQ_REF_LOCK_BIT = (1 << 17)
DIFI_STATE_EVENT_IND_CALIBRATED_TIME_BIT = (1 << 19)

# data packet payload format field - standard context
DIFI_DATA_PACKET_PAYLOAD_FORMAT_FIELD_PACKING_METHOD = 1 
DIFI_DATA_PACKET_PAYLOAD_FORMAT_FIELD_REAL_COMPLEX_TYPE = 1 
DIFI_DATA_PACKET_PAYLOAD_FORMAT_FIELD_DATA_ITEM_FORMAT = 0 
DIFI_DATA_PACKET_PAYLOAD_FORMAT_FIELD_SAMPLE_COMPONENT_REPEAT_IND = 0 
DIFI_DATA_PACKET_PAYLOAD_FORMAT_FIELD_EVENT_TAG_SIZE = 0 
DIFI_DATA_PACKET_PAYLOAD_FORMAT_FIELD_CHANNEL_TAG_SIZE = 0 

# protocol
UDP_PROTO = b'\x11' 

# file stuff
DIFI_COMPLIANT_FILE_PREFIX = "difi-compliant-"
DIFI_NONCOMPLIANT_FILE_PREFIX = "difi-noncompliant"

DIFI_COMPLIANT_COUNT_FILE_PREFIX = "difi-compliant-count"
DIFI_NONCOMPLIANT_COUNT_FILE_PREFIX = "difi-noncompliant-count"

DIFI_STANDARD_CONTEXT = "context"
DIFI_VERSION_CONTEXT = "version"
DIFI_DATA = "data"

DIFI_FILE_EXTENSION = ".dat"