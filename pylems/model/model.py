"""
Model storage

@author: Gautham Ganapathy
@organization: Textensor (http://textensor.com)
@contact: gautham@textensor.com, gautham@lisphacker.org
"""

from pylems.base.errors import ModelError
from pylems.model.context import Contextual

class Model(Contextual):
    """
    Store the model read from a LEMS file.
    """

    def __init__(self):
        """
        Constructor.
        """

        super(Model, self).__init__()
        
        self.default_run = []
        """ Names of simulations to run.
        @type: string """

        self.dimensions = None
        """ Dictionary of references to dimensions defined in the model.
        @type: dict(string -> pylems.model.simple.Dimension) """

        self.units = None
        """ Dictionary of references to units defined in the model.
        @type: dict(string -> pylems.model.simple.Unit) """

        self.context = None
        """ Root context
        @type: pylems.model.context.Context """

    def set_default_run(self, default_run):
        """
        Set the name of the default simulation to run.
        
        @param default_run: Name of a simulation to run by default
        @type default_run: string """
        self.default_run += [default_run]

    def add_dimension(self, dimension):
        """
        Adds a dimension to the list of defined dimensions.

        @param dimension: Dimension to be added to the model.
        @type dimension: pylems.base.units.Dimension

        @raise ModelError: Raised when the dimension is already defined.
        """

        if self.dimensions == None:
            self.dimensions = dict()

        if dimension.name in self.dimensions:
            raise ModelError('Duplicate dimension - ' + dimension.name)
        else:
            self.dimensions[dimension.name] = dimension
        
    def add_unit(self, unit):
        """
        Adds a unit to the list of defined units.

        @param unit: Unit to be added to the model.
        @type unit: pylems.base.units.Unit

        @raise ModelError: Raised when the unit is already defined.
        """

        if self.units == None:
            self.units = dict()

        if unit.symbol in self.units:
            raise ModelError('Duplicate unit - ' + unit.symbol)
        else:
            self.units[unit.symbol] = unit

    tab = '  '

    def regime2str(self, regime, prefix):
        s = ''
        if regime.state_variables:
            s += prefix + Model.tab + 'State variables:\n'
            for svn in regime.state_variables:
                sv = regime.state_variables[svn]
                s += prefix + Model.tab*2 + sv.name
                if sv.exposure:
                    s += ' (exposed as ' + sv.exposure + ')'
                s += ': ' + sv.dimension + '\n'

        if regime.time_derivatives:
            s += prefix + Model.tab + 'Time derivatives:\n'
            for tdv in regime.time_derivatives:
                td = regime.time_derivatives[tdv]
                s += prefix + Model.tab*2 + td.variable + ' = ' + td.value\
                     + ' | ' + str(td.expression_tree) + '\n'

        return s
    
    def behavior2str(self, behavior, prefix):
        s = prefix
        if behavior.name != '':
            s += name
        else:
            s += '*'
        s += '\n'

        if behavior.default_regime:
            s += prefix + Model.tab + 'Default regime:\n'
            s += self.regime2str(behavior.default_regime,
                                 prefix + Model.tab)


        return s

    def context2str(self, context, prefix):
        s = ''
        prefix = prefix + Model.tab
        if context.component_types:
            s += prefix + 'Component types:\n'
            for tn in context.component_types:
                t = context.component_types[tn]
                s += prefix + Model.tab + t.name
                if t.extends:
                    s += ' (extends ' + t.extends + ')'
                s += '\n'
                s += self.context2str(t.context, prefix + Model.tab)

        if context.components:
            s += prefix + 'Components:\n'
            for cn in context.components:
                c = context.components[cn]
                s += prefix + Model.tab + c.id
                if c.component_type:
                    s += ': ' + c.component_type + '\n'
                else:
                    s+= ' (extends ' + c.extends + ')' + '\n'
                s += self.context2str(c.context, prefix + Model.tab)

        if context.exposures:
            s += prefix + 'Exposures:\n'
            for name in context.exposures:
                s += prefix + Model.tab + name + '\n'

        if context.behavior_profiles:
            s += prefix + 'Behavior profiles:\n'
            for name in context.behavior_profiles:
                behavior = context.behavior_profiles[name]
                s += self.behavior2str(behavior, prefix + Model.tab*2)

        return s
    
    def __str__(self):
        s = ''

        s += 'Default run:\n'
        for run in self.default_run:
            s += Model.tab + run + '\n'
        
        s += 'Dimensions:\n'
        if self.dimensions != None:
            for d in self.dimensions:
                s += Model.tab + d + '\n'

        s += 'Units:\n'
        if self.units != None:
            for u in self.units:
                s += Model.tab + u + '\n'

        if self.context:
            s += 'Global context:\n'
            s += self.context2str(self.context, '')
            
        return s
