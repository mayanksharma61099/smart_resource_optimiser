# smart_resource_optimiser

Imagine a startup experiencing fluctuating traffic. During peak hours, their website slows down, impacting customer experience. During off-peak hours, they're paying for idle resources. Your tool steps in, automatically adjusting the number of EC2 instances to match the demand, saving them money and ensuring smooth performance.

Many organizations struggle with the sheer complexity and cost of managing cloud resources. They often over-provision, leading to wasted spending, or under-provision, causing performance bottlenecks. We need a way to dynamically optimize resource allocation based on real-time demand.

"Smart Resource Optimizer" - A Python-based tool deployed on AWS Lambda that monitors EC2 instance utilization (CPU, memory, network) using CloudWatch metrics. It then uses simple threshold-based logic to automatically scale instances up or down.

