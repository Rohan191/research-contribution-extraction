import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence, pad_sequence, pad_packed_sequence
import torch


class LSTMNet(nn.Module):
    """
    LSTM Model followed by a fully connected layer and a sigmoid layer
    """
    def __init__(self, embed_size, hidden_size):
        super(LSTMNet, self).__init__()
        self.hidden_size = hidden_size
        self.embed_size = embed_size
        self.lstm = nn.LSTM(self.embed_size, self.hidden_size, batch_first=True, num_layers=1)
        
        # FC layer to convert hidden size vector to output size
        self.fc = nn.Linear(self.hidden_size, 1)
        self.initparams()
        
    def initparams(self):
        self.fc.weight.data.uniform_(-0.1, 0.1)
        self.fc.bias.data.fill_(0)
        self.lstm.weight_hh_l0.data.uniform_(-0.1, 0.1)
        self.lstm.weight_ih_l0.data.uniform_(-0.1, 0.1)
        self.lstm.bias_hh_l0.data.fill_(0)
        self.lstm.bias_ih_l0.data.fill_(0)
        
    def forward(self, x, h_0, c_0):
        """ Takes a packed padded sequence as input and initial hidden and cells states. 
        Returns sigmoid output for every lstm cell in every batch.
        """
        packed_output, (h_n, c_n) = self.lstm(x, (h_0, c_0))
        x, input_sizes = pad_packed_sequence(packed_output, batch_first=True)
        x = self.fc(x)
        x = torch.sigmoid(x)
        return x