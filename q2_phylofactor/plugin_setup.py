import importlib
import q2_phylofactor
import qiime2

from qiime2.plugin import (
    Plugin,
    Str,
    Int,
    Metadata,
    SemanticType)

from q2_phylofactor._phylofactor import phylofactor
from q2_types.tree import Phylogeny, Unrooted
from q2_types.feature_table import FeatureTable, Frequency
from q2_types.feature_data import FeatureData
from q2_phylofactor import Factors, FactorsFormat, FactorsDirFmt

_CHOICE_OPT = {'F', 'var', 'none'}

plugin = Plugin(
    name='phylofactor',
    version=q2_phylofactor.__version__,
    website='https://github.com/johnchase/q2-phylofactor',
    package='q2_phylofactor',
    description='Plugin defining clades associated with given metadata '
                'category`',
    short_description='Plugin for running phylofactor',
    )

plugin.methods.register_function(
    function=phylofactor,
    inputs={'table': FeatureTable[Frequency],
            'phylogeny': Phylogeny[Unrooted],
            },

    parameters={
        'metadata': Metadata,
        'formula': Str,
        'family': Str,
        'choice': Str % qiime2.plugin.Choices(_CHOICE_OPT),
        'nfactors': Int,
        'ncores': Int
    },
    outputs=[
        ('featuretable', FeatureTable[Frequency]),
        ('tree', Phylogeny[Unrooted]),
        ('factors', FeatureData[Factors])
    ],
    input_descriptions={'table': 'The sample by observation table',
                        'phylogeny': ('The phylogenetic tree describing the '
                                      'relationship of the observations in '
                                      'table')
                        },
    parameter_descriptions={
        },
    output_descriptions={
        },
    name='Run Phylofactor',
    description='Phylofactor defines clades that are associated with '
                'metadata columns of interest'
)

plugin.register_formats(FactorsFormat, FactorsDirFmt)
plugin.register_semantic_types(Factors)
plugin.register_semantic_type_to_format(FeatureData[Factors], FactorsDirFmt)
importlib.import_module('q2_phylofactor._transform')
