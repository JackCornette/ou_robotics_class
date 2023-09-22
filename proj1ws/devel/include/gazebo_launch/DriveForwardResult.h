// Generated by gencpp from file gazebo_launch/DriveForwardResult.msg
// DO NOT EDIT!


#ifndef GAZEBO_LAUNCH_MESSAGE_DRIVEFORWARDRESULT_H
#define GAZEBO_LAUNCH_MESSAGE_DRIVEFORWARDRESULT_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace gazebo_launch
{
template <class ContainerAllocator>
struct DriveForwardResult_
{
  typedef DriveForwardResult_<ContainerAllocator> Type;

  DriveForwardResult_()
    : success(false)  {
    }
  DriveForwardResult_(const ContainerAllocator& _alloc)
    : success(false)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;





  typedef boost::shared_ptr< ::gazebo_launch::DriveForwardResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::gazebo_launch::DriveForwardResult_<ContainerAllocator> const> ConstPtr;

}; // struct DriveForwardResult_

typedef ::gazebo_launch::DriveForwardResult_<std::allocator<void> > DriveForwardResult;

typedef boost::shared_ptr< ::gazebo_launch::DriveForwardResult > DriveForwardResultPtr;
typedef boost::shared_ptr< ::gazebo_launch::DriveForwardResult const> DriveForwardResultConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::gazebo_launch::DriveForwardResult_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::gazebo_launch::DriveForwardResult_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::gazebo_launch::DriveForwardResult_<ContainerAllocator1> & lhs, const ::gazebo_launch::DriveForwardResult_<ContainerAllocator2> & rhs)
{
  return lhs.success == rhs.success;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::gazebo_launch::DriveForwardResult_<ContainerAllocator1> & lhs, const ::gazebo_launch::DriveForwardResult_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace gazebo_launch

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::gazebo_launch::DriveForwardResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::gazebo_launch::DriveForwardResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::gazebo_launch::DriveForwardResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::gazebo_launch::DriveForwardResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::gazebo_launch::DriveForwardResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::gazebo_launch::DriveForwardResult_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::gazebo_launch::DriveForwardResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const ::gazebo_launch::DriveForwardResult_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::gazebo_launch::DriveForwardResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "gazebo_launch/DriveForwardResult";
  }

  static const char* value(const ::gazebo_launch::DriveForwardResult_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::gazebo_launch::DriveForwardResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#result\n"
"bool success\n"
;
  }

  static const char* value(const ::gazebo_launch::DriveForwardResult_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::gazebo_launch::DriveForwardResult_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct DriveForwardResult_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::gazebo_launch::DriveForwardResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::gazebo_launch::DriveForwardResult_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GAZEBO_LAUNCH_MESSAGE_DRIVEFORWARDRESULT_H