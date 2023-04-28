# Integrated Calendar for Odoo

The Integrated Calendar module for Odoo combines various calendar views from different modules into a single, unified calendar app. This allows users to manage and monitor activities across different business areas more efficiently.

## Features

- Consolidated view of important dates from multiple modules:
  - Sales meetings
  - Warehouse scheduled dates
  - Helpdesk support dates
  - Project and task dates
- Month view as the default calendar view, with optional week and day views
- Calendar items display the source-document number, partner name, and execution times
- Calendar items color-coded based on their originating module for easy visual distinction
- Designed for expandability, allowing for the inclusion of additional dates from other modules in the future



## Installation

1. This module is depend on an external library "mako"
Install this python package (in python environment that you are using to run odoo)
and restart the odoo service 

2. Download or clone this repository to your local machine.
3. Copy the `super_calendar` folder to your Odoo addons directory (e.g., `/odoo/addons`).
4. Update the addons list in your Odoo instance:
   - Go to the "Apps" menu
   - Click on the "Update Apps List" menu item
   - Click the "Update" button in the dialog that appears
5. Install the Integrated Calendar module:
   - Remove the "Apps" filter in the search bar
   - Search for "Integrated Calendar"
   - Click the "Install" button on the Integrated Calendar module

## Usage
1. After installing the module you can go to "Integrated Calendar" > Configuration > Configurators
and create a new configurator. 
2. Then, you can use the "Generate Calendar" button or wait for the scheduled action ("Generate Calendar Records") to be run.

When the calendar is generated, you can visualize it by the "Integrated Calendar" main menu.

## Dependencies

This module depends on the following Odoo modules:

- `calendar`
- `sale`
- `stock`
- `helpdesk`
- `project`

Ensure that these modules are installed and functional in your Odoo instance before installing the Integrated Calendar module.

## Customization

This module can be customized to include additional dates from other modules or to modify the appearance and behavior of the integrated calendar view. Consult the Odoo documentation and the provided code for guidance on making customizations to suit your specific requirements.

## Support

If you encounter any issues or require assistance with the Integrated Calendar module, please refer to the [Odoo documentation](https://www.odoo.com/documentation/14.0/) and consult the Odoo community for further guidance and support.

## License

This module is released under the [LGPL-3.0 License](https://www.gnu.org/licenses/lgpl-3.0.html).
