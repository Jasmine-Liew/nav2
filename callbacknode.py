import rclpy
from rclpy.node import Node

class TestParamsCallback(Node):
    def __init__(self):
        super().__init__('test_params_callback_rclpy')
        self.declare_parameter('camera_device_port', '/dev/ttyACM0')
        self.declare_parameter('simulation_mode', False)
        self.declare_parameter('battery_percentage_warning', 15.0)

        self.camera_device_port_ = self.get_parameter('camera_device_port').value
        self.simulation_mode_ = self.get_parameter('simulation_mode').value
        self.battery_percentage_warning_ = self.get_parameter('battery_percentage_warning').value

def main(args=None):
    rclpy.init(args=args)
    node = TestParamsCallback()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
    
