---
template: custom/contentpage.html
# status: new
title: Lorem ipsum dolor sit amet
description: Nullam urna elit, malesuada eget finibus ut, ac tortor.  
# subtitle: this is a subtitle
hero_text: Test Page
hero_image1: https://static.igem.wiki/teams/5016/wiki/education-presentation-picture-2.jpg
# hero_image2: https://static.igem.wiki/teams/5016/wiki/tum-cit.png
hero_image3: https://static.igem.wiki/teams/5016/wiki/roche.svg
hero_image4: https://static.igem.wiki/teams/5016/wiki/freunde-der-tum.svg
---

# Test page

page for testing[^1]

## Test  Structure
this is the structure test
### ABC
ABC some content
### DEF
DEF some content

## Hover

[Hover me](https://example.com "I'm a tooltip!")

:material-information-outline:{ title="Important information" }

do these changes propagate again?

## Code

```python title="bubble_sort.py" linenums="227" hl_lines="2-6"
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.datasets import Planetoid
import torch_geometric.nn as pyg_nn

# Load the Cora dataset from PyTorch Geometric
dataset = Planetoid(root='data/Cora', name='Cora')

# Define a Graph Neural Network class
class GNNModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_classes):
        super(GNNModel, self).__init__()
        self.conv1 = pyg_nn.GCNConv(input_dim, hidden_dim)
        self.conv2 = pyg_nn.GCNConv(hidden_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        x = F.relu(x)
        x = pyg_nn.global_mean_pool(x, data.batch)
        x = self.fc(x)
        return F.log_softmax(x, dim=1)

# Instantiate the model
input_dim = dataset.num_node_features
hidden_dim = 64
num_classes = dataset.num_classes
model = GNNModel(input_dim, hidden_dim, num_classes)

# Define loss function and optimizer
criterion = nn.NLLLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Training loop
def train():
    model.train()
    optimizer.zero_grad()
    output = model(dataset[0])  # Pass the first graph in the dataset
    loss = criterion(output, dataset[0].y)
    loss.backward()
    optimizer.step()

# Training for a few epochs
for epoch in range(100):
    train()
    print(f'Epoch: {epoch + 1}, Loss: {loss.item()}')


print('Hello World')
```

``` yaml
theme:
  features:
    - content.code.annotate # (1)
```

1.  :man_raising_hand: I'm a code annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be written in Markdown.

## Figures

!!! example "Trends in Polypharmacy"
    <figure markdown>
        ![Image title](img/plot1-dark.png#only-dark){ width=600" }
        ![Image title](img/plot1-light.png#only-light){ width=600" }
        
    <figcaption>Trends in polypharmacy among adults in the Netherlands 1999–2014, stratified by age.[^3]</figcaption>
    </figure>

## Keys

++cmd+option+delete++
=/=
(c)++alt+f4++(tm)

## Citations

this is a test[^2]
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque quis urna nibh. Phasellus sed dui tempor, dignissim quam vel, tristique elit. Mauris commodo ex posuere sapien elementum ullamcorper. Mauris sed auctor velit, a congue magna. Aliquam quis tempus libero. Cras neque diam, placerat varius dictum et, ullamcorper vitae neque. Etiam sit amet risus laoreet, mattis mi ac, suscipit justo. Suspendisse libero dui, facilisis vel vestibulum non, consectetur quis justo. Suspendisse potenti. Donec et quam at tortor elementum vehicula vel sed sem. Phasellus hendrerit quis justo non gravida. Vestibulum suscipit dolor vel felis cursus ultricies.[^2]

## Boxes

!!! example "test for testing stuff"

    === "Unordered List"

        ``` markdown
        * Sed sagittis eleifend rutrum
        * Donec vitae suscipit est
        * Nulla tempor lobortis orci
        ```

    === "Ordered List"

        ``` markdown
        1. Sed sagittis eleifend rutrum
        2. Donec vitae suscipit est
        3. Nulla tempor lobortis orci
        ```

    !!! note "Inside"

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

!!! note "Outside"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

## Table

| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |
| `GET`       | :material-check:     Fetch resource  |


!!! info inline end "Lorem ipsum"

    Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Nulla et euismod nulla.
    Curabitur feugiat, tortor non consequat
    finibus, justo purus auctor massa, nec
    semper lorem quam in massa.


## Lipsum
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque quis urna nibh. Phasellus sed dui tempor, dignissim quam vel, tristique elit. Mauris commodo ex posuere sapien elementum ullamcorper. Mauris sed auctor velit, a congue magna. Aliquam quis tempus libero. Cras neque diam, placerat varius dictum et, ullamcorper vitae neque. Etiam sit amet risus laoreet, mattis mi ac, suscipit justo. Suspendisse libero dui, facilisis vel vestibulum non, consectetur quis justo. Suspendisse potenti. Donec et quam at tortor elementum vehicula vel sed sem. Phasellus hendrerit quis justo non gravida. Vestibulum suscipit dolor vel felis cursus ultricies.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque quis urna nibh. Phasellus sed dui tempor, dignissim quam vel, tristique elit. Mauris commodo ex posuere sapien elementum ullamcorper. Mauris sed auctor velit, a congue magna. Aliquam quis tempus libero. Cras neque diam, placerat varius dictum et, ullamcorper vitae neque. Etiam sit amet risus laoreet, mattis mi ac, suscipit justo. Suspendisse libero dui, facilisis vel vestibulum non, consectetur quis justo. Suspendisse potenti. Donec et quam at tortor elementum vehicula vel sed sem. Phasellus hendrerit quis justo non gravida. Vestibulum suscipit dolor vel felis cursus ultricies.

## Search Test
this is a test for search

## Link

[Link text Here](https://google.com)

## TitleA

content\
content

## TitleB

content\
content
## TitleC

content\
content\
content

## TitleD

content\
content\
content\
content\
content\
content\
content\
content\
content\
content\
content\
content\
content\
content\
content\

## TitleE

content\
content\
content\
content\
content\
content\
content\
content\
content\
content\
content\
content\
content\
content\
content\

## References

[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.

[^2]:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

[^3]: Oktora, Monika, et al. "Trends in Polypharmacy and Dispensed Drugs among Adults in the Netherlands as Compared to the United States." PLOS ONE, vol. 14, no. 3, 2019, p. e0214240,  [https://doi.org/10.1371/journal.pone.0214240](https://doi.org/10.1371/journal.pone.0214240).