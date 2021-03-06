"""
this file contains tooltips messages values
"""

name = '''REQUIRED. Name of the dataset.'''

bids_version = '''REQUIRED. The version of the BIDS standard that was used.'''

dataset_type =\
    '''RECOMMENDED. The interpretaton of the dataset. MUST be one of "raw" 
or "derivative". For backwards compatibility, the default value is "raw".'''

dataset_license =\
    '''RECOMMENDED. The license for the dataset. The use of license name 
abbreviations is RECOMMENDED for specifying a license (see Appendix II). 
The corresponding full license text MAY be specified in an additional
LICENSE file.'''

license_pd =\
    '''Public Domain: No license required for any purpose;
the work is not subject to copyright in any jurisdiction.'''

license_pddl =\
    '''Open Data Commons Public Domain Dedication and License:
License to assign public domain like permissions without giving up the
copyright: http://opendatacommons.org/licenses/pddl/'''

license_cc0 =\
    '''Creative Commons Zero 1.0 Universal.:
use this if you are a holder of copyright or database rights, and you wish
to waive all your interests in your work worldwide:
http://opendatacommons.org/licenses/cc0/'''

authors =\
    '''OPTIONAL. List of individuals who contributed to the creation/curation of
the dataset.'''

acknowledgements =\
    '''OPTIONAL. Text acknowledging contributions of individuals or
institutions beyond those listed in Authors or Funding.'''

how_to_ack =\
    '''OPTIONAL. Text containing instructions on how researchers using this
dataset should acknowledge the original authors. This field can also be used
to define a publication that should be cited in publications that use the
dataset.'''

funding = '''OPTIONAL. List of sources of funding (grant numbers).'''

ethics_approval =\
    '''OPTIONAL. List of ethics committee approvals of the research protocols
and/or protocol identifiers.'''

ref_and_links =\
    '''OPTIONAL. List of references to publication that contain information on
the dataset, or links.'''

dataset_doi =\
    '''OPTIONAL. The Document Object Identifier of the dataset
(not the corresponding paper).'''

generated_by =\
    '''REQUIRED. List of [objects][object] with at least one element.'''

gen_name =\
    '''REQUIRED. Name of the pipeline or process that generated the outputs.
Use "Manual" to indicate the derivatives were generated by hand, or adjusted
manually after an initial run of an automated pipeline.'''

gen_version = '''RECOMMENDED. Version of the pipeline.'''

gen_description = \
    '''OPTIONAL. Plain-text description of the pipeline or process that
generated the outputs. RECOMMENDED if Name is "Manual".'''

gen_code_url = \
    '''OPTIONAL. URL where the code used to generate the derivatives
may be found.'''

gen_container = \
    '''OPTIONAL. [Object][object] specifying the location and relevant
attributes of software container image used to produce the derivative.
Valid fields in this object include Type, Tag and URI.'''

sources_datasets = \
    '''RECOMMENDED. A list of [objects][object] specifying the locations and
relevant attributes of all source datasets. Valid fields in each object
include URL, DOI, and Version.'''
